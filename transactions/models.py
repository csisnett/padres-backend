from djmoney.models.fields import MoneyField
from django.db import models
from utils.mixins import UUIDable, Descriptionable



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
    possessions = models.OneToOneField('Owner', on_delete='PROTECT', related_name='companies')

    app_label = 'transactions'

class Contract(UUIDable, Descriptionable, models.Model):
    title = models.CharField(max_length=140)
    approved_by = models.ManyToManyField('padres.Person')
    companies = models.ManyToManyField('Company')

class BankAccount(Ownable, models.Model):

    balance = MoneyField(max_digits=19, decimal_places=2)
    transactions = models.ManyToManyField('BankAccount')

    def new_balance(self, amount, sender):

        return self.balance + amount


    def currencydecimal(self):
        return self.balance.currency


class Thing(Ownable, UUIDable, Descriptionable, models.Model):
    name = models.CharField(max_length=110)

class Owner(UUIDable, models.Model):
    pass


