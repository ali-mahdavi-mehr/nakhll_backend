from abc import ABC, abstractmethod
from django.shortcuts import redirect
from django.conf import settings
from django.utils.translation import ugettext as _
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from payoff.models import Transaction, TransactionResult
from zeep import Client


class PaymentMethod(ABC):
    def __init__(self, transaction):
        self.transaction = transaction
        self.client = Client(settings.PAYMENT_WSDL)
        self.payment_method = self.client.get_type('ns0:PaymentMethod')
        self.payment_method_type = self.client.get_type('ns0:PaymentMethodType')

    def get_payment_method(self):
        return self.payment_method(
            paymentMethodType=self.payment_method_type(
                id=self.transaction.payment_method
            )
        )
    
    @abstractmethod
    def do_transaction(self, transaction):
        pass


class Pec(PaymentMethod):

    def __init__(self):
        # TODO: These errors should be handled better with better messages
        pec_pin = settings.get('PEC_PIN')
        callback_url = settings.get('CALLBACKURL')
        if not pec_pin:
            raise ValidationError(_('در حال حاضر امکان اتصال به درگاه بانکی وجود ندارد'))
        if not callback_url:
            raise ValidationError(_('در حال حاضر امکان اتصال به درگاه بانکی وجود ندارد'))
        self.pec_pin = pec_pin
        self.callback_url = callback_url


    def initiate_payment(self, transaction):
        ''' Get invoice, exchange with token and redirect user to payment page '''
        token = self._get_token(transaction)
        return redirect(f'https://pec.shaparak.ir/NewIPG/?token={token}')

    def complete_payment(self, transaction):
        ''' save IGP to DB, Check validation and send confrim/reverse request to IPG '''
        if self.transaction.is_succeed():
            self._validate_transaction(transaction)
            self._close_transaction(transaction)
        else:
            self._reverse_transaction(transaction)


    def _close_transaction(self, transaction):
        ''' Change everythings status to DONE, reduce inventory, create alert, etc '''
        transaction.invoice.cart.close() # TODO: This should change cart status to complete
        transaction.invoice.close() # TODO: This should change invoice status to complete, create alert,
                                            # send email and sms to customer and shop owner, reduce stock, etc.
                                            # create an order for shop owner to send product to customer



    def _validate_transaction(self, transaction):
        ''' Send request to IGP validation url and validate transaction '''
        token = transaction.token
        pec_pin = self.pec_pin
        confirm_service = self._get_confirm_service()
        request_data = confirm_service(Token=token, LoginAccount=pec_pin)
        result = confirm_service.service.ConfirmPaymentRequest(request_data)
        token = result.get('token', 0)
        if token <= 0:
            # TODO: create alert for support to handle this
            pass




    def _get_sale_serivce():
        # TODO we must handle exceptions of SOAP connections
        return Client('https://pec.shaparak.ir/NewIPGServices/Sale/SaleService.asmx?wsdl')

    def _get_confirm_service():
        # TODO we must handle exceptions of SOAP connections
        return Client('https://pec.shaparak.ir/NewIPGServices/Confirm/ConfirmService.asmx?wsdl')

    def _get_token(self, transaction):
        ''' Get sale service and send invocie data to it, return token if invoice data is valid '''
        ClientSaleRequestData = self._get_client_sale_request_data()
        request_data = ClientSaleRequestData(
                LoginAccount=self.pec_pin,
                Amount=transaction.amount,
                OrderId=transaction.order_number,
                CallBackUrl=self.callback_url,
                AdditionalData=transaction.description,
                Originator=transaction.mobile)
        saleService = self._get_sale_serivce()
        result = saleService.service.SalePaymentRequest(request_data)
        self._save_sale_payment_result(result)
        if result.get('status') != 0 or result.get('Token', 0) <= 0:
            raise ValidationError(_('خطایی در پرداخت رخ داده است'))
        return result.get('token')

    def _save_sale_payment_result(self, result):
        ''' Store result of token request from IPG to DB'''
        self.transaction.token_request_status = result.get('status')
        self.transaction.token_request_message = result.get('message')
        self.transaction.token = result.get('token')
        self.transaction.save()

    def _get_client_sale_request_data(self):
        saleService = self._get_sale_serivce()
        ClientSaleRequestData = saleService.get_type('ns0:ClientSaleRequestData')
        return ClientSaleRequestData


class ZarinPal(PaymentMethod):
    def __init__(self):
        pass
    # def zarin_pay():
    #     result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    #     if result.Status == 100:
    #         return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    #     else:
    #         return HttpResponse('Error code: ' + str(result.Status))




class Payment():
    def __init__(self, request):
        self.request = request


    def get_ipg_class(self, ipg_type):
        if ipg_type == Transaction.IPGTypes.PEC:
            return Pec
        if ipg_type == Transaction.IPGTypes.ZARINPAL:
            return ZarinPal

    def start_payment_process(self, data):
        self.transaction = Transaction.objects.create(**data)
        ipg_class = self.get_ipg_class(self.transaction.ipg_type)
        ipg = ipg_class()
        ipg.initiate_payment(self.transaction)


    def transaction_callback(self, data):
        transaction_result = TransactionResult.objects.create(**data)
        try:
            transaction = Transaction.objects.get(invoice_id=data.get('order_id'))
            transaction_result.transaction = transaction
            transaction_result.save()

            ipg_class = self.get_ipg_class(transaction.ipg_type)
            ipg = ipg_class()
            ipg.complete_payment(transaction_result)
        except:
            self.no_transaction_error(transaction_result)



    def no_transaction_error(self, transaction_result):
        ''' Set alert for admin to check this transaction '''
