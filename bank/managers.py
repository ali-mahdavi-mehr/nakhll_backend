from django.db import models, transaction
from django.db.models import Q, Sum
from bank.account_requests import CreateRequest
from bank.constants import NAKHLL_ACCOUNT_ID, RequestStatuses, RequestTypes


class AppendOnlyMixin:
    '''we also have modifying object from save method
    and we have bulk_update method
    '''

    def save(self, *args, **kwargs):
        if self.pk is not None:
            raise Exception('you can\'t update coin')
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise Exception('you can\'t delete coin')

    def update(self, *args, **kwargs):
        raise Exception('you can\'t update coin')


class AccountManager(models.Manager):
    @property
    def nakhll_account(self):
        return self.get_queryset().get(pk=NAKHLL_ACCOUNT_ID)

    @property
    def nakhll_account_for_update(self):
        return self.get_queryset().select_for_update().get(pk=NAKHLL_ACCOUNT_ID)


class AccountRequestQuerySet(models.QuerySet):
    def filter_account_requests(self, account):
        return self.filter(Q(from_account=account) | Q(to_account=account))

    def request_coins_report(self):
        return self.values(
            'request_type', 'status').annotate(
            coins=Sum('value'))



class AccountRequestManager(models.Manager):
    def get_queryset(self):
        return AccountRequestQuerySet(self.model, using=self._db)

    def create(self, *args, **kwargs):
        self._for_write = True
        self.model(*args, **kwargs).create()

    def account_request_coins_report(self, account):
        queryset = self.get_queryset().filter_account_requests(
            account).request_coins_report()
        self._update_request_and_status_to_labels(queryset)
        return queryset

    def _update_request_and_status_to_labels(self, queryset):
        list(map
             (lambda row: row.update(
                 {
                     'request_type': RequestTypes(row['request_type']).label,
                     'status': RequestStatuses(row['status']).label
                 }
             ), queryset))
