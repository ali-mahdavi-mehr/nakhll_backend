from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from cart.managers import CartManager
from .exceptions import EmptyCartException
from .models import Invoice
from .permissions import IsInvoiceOwner
from .serializers import InvoiceRetrieveSerializer, InvoiceWriteSerializer


class InvoiceViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin, mixins.ListModelMixin):
    """User Invoices ViewSet. User can only create, list and retrieve

    Invoices are created when a user tries to  checkout a cart. User can
    view all his invoices in his/her profile.

    Permissions:
        IsInvoiceOwner: Only the user who created the invoice can view it.
        IsAuthenticated: Only authenticated users can create, list and retrieve

    """
    permission_classes = [IsInvoiceOwner, permissions.IsAuthenticated, ]
    queryset = Invoice.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return InvoiceRetrieveSerializer
        return InvoiceWriteSerializer

    def create(self, request, *args, **kwargs):
        invoice = self._create_invoice(request)
        serializer = InvoiceRetrieveSerializer(invoice)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_200_OK,
                        headers=headers)

    def _create_invoice(self, request):
        """Create an invoice from user cart"""
        cart = CartManager.user_cart(request.user)
        if not cart.items.all():
            raise EmptyCartException
        invoice = cart.convert_to_invoice()
        return invoice

    @action(methods=['POST'], detail=True)
    def pay(self, request, pk):
        """Get an invoice and send it to payment app

            Request for invoice should came from owner.
            Invoice should sent to payment to initiate payment
        """
        invoice = self.get_object()
        return invoice.send_to_payment()

    @action(methods=['POST'], detail=True)
    def fill_cart(self, request, pk):
        """Fill users cart with invoice items

        This function initialy created to fill user's cart when user returns
        from payment gateway with failed payment, where user's cart is
        converted to invoice before payment.
       """
        invoice = self.get_object()
        invoice.fill_cart()
        return Response({'status': 'success'})
