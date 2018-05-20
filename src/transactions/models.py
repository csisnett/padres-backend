from djmoney.models.fields import MoneyField
from django.db import models
from utils.mixins import UUIDable, Descriptionable
from annoying.fields import AutoOneToOneField

"""
class Transactionable(models.Model):
    
    Transaction Mixin 
    Defines the attributes and relations of a Transaction
    Transactions inherit from TransactionMixin

    transaction is  inheritedTransaction(TransactionMixin, Basemodel)

    interpretation: a transaction with a sender and a receiver.


    example:
    transaction = transaction(
        title='Pago de contrato de IDAAN',
        description='Awful',
        buyer=UUID, UUID,
        seller=UUID, UUID,
    )
    
    sender = models.ForeignKey('Account', on_delete='')
    receiver = models.ForeignKey('Account')

    class Meta:
        abstract = True


class MonetaryTransaction(Transactionable, models.Model):
    
    amount_paid = MoneyField(decimal_places=2, default_currency='USD')

    object_sold = models.ManyToManyField('Thing')

"""


class Ownable(models.Model):
    """ Describes any thing that can be owned"""

    owners = models.ManyToManyField('Owner')
    
    class Meta:
        abstract = True

class Company(Ownable, UUIDable, Descriptionable, models.Model):
    name = models.CharField(max_length=130)
    owner = models.AutoOneToOneField('Owner', on_delete='PROTECT', related_name='companies')



class Contract(UUIDable, Descriptionable, models.Model):
    title = models.CharField(max_length=140)
    supported_by = models.ManyToManyField('padres.Person', related_name='supported_contracts')
    signed_by = models.ManyToManyField('padres.Person', related_name='signed_contracts')
    companies = models.ManyToManyField('Company')
    payments = models.ManyToManyField('Payment', blank=True)
    

class BankAccount(UUIDable, Ownable, models.Model):

    balance = MoneyField(max_digits=19, decimal_places=2)
    transactions = models.ManyToManyField('BankAccount', blank=True, null=True)



class Thing(Ownable, UUIDable, Descriptionable, models.Model):
    name = models.CharField(max_length=110)
    value = MoneyField(max_digits=19, decimal_places=2)

#for alternatives to generic relations go to https://lukeplant.me.uk/blog/posts/avoid-django-genericforeignkey/

class Owner(UUIDable, models.Model):
    
    pass

class Payment(UUIDable, models.Model):
    sender = models.ForeignKey('Owner')
    receiver = models.ForeignKey('Owner')
    amount = MoneyField(max_digits=19, decimal_places=2)
    authorized_by = models.ManytoManyField('padres.Person', blank=True, null=True)
    event = models.ForeignKey('padres.Event', null=True)
    #reasonable or not field
    #type of payment: donation, salary, bribe
