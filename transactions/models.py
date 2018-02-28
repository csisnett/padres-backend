from djmoney.models.fields import MoneyField
from django.db import models

class MonetaryTransaction(TransactionMixin):
    
    amount = MoneyField(decimal_places=2, default_currency='USD') 

class TransactionMixin(models.Model):
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField()
    sender = models.ForeignKey(Account)
    receiver = models.ForeignKey(Account)

    class Meta:
        abstract = True

class Company(models.Model):
    title = models.CharField(max_length=130)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)
    description = models.TextField()
    owners = models.ManyToManyField('padres.Person')

class Contract(models.Model):
    title = models.CharField(max_length=140)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    description = models.TextField()

class Account(models.Model):
    ownership = ...