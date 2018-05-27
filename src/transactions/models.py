from djmoney.models.fields import MoneyField
from django.db import models
from utils.mixins import UUIDable, Descriptionable
from .managers import CompanyManager


class Ownable(models.Model):
    """ Describes any thing that can be owned"""

    owners = models.ManyToManyField('Owner', blank=True)
    
    class Meta:
        abstract = True



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
    


class Company(Ownable, UUIDable, Descriptionable, models.Model):
    name = models.CharField(max_length=130)
    ownership = models.OneToOneField('Owner', on_delete='PROTECT',
     related_name='companies', blank=True, null=True)

    objects = CompanyManager()


class Payment(UUIDable, models.Model):

    PAYMENT_REASONS = (
    ('S', "Salario"),
    ('C', 'Coima'),
    ('SIN', 'Sin Justificación'),
    ('B', "Bono"),
    ('SOB', "Soborno"),
    ('DON', "Donación"),
    ('CON', "Pago por Contrato")
    )
    reason = models.CharField(max_length=3, choices=PAYMENT_REASONS, default='SIN')

    sender = models.ForeignKey('Owner', on_delete='PROTECT', related_name='money_sent')
    receiver = models.ForeignKey('Owner', on_delete='PROTECT', related_name='money_received')
    amount = MoneyField(max_digits=19, decimal_places=2)
    authorized_by = models.ManyToManyField('padres.Person', blank=True, null=True)
    event = models.ForeignKey('padres.Event', null=True, on_delete='PROTECT')
    repetition = models.PositiveSmallIntegerField(default=1)
    total_amount = MoneyField(max_digits=19, decimal_places=2)

    
    #reasonable or not field
    #type of payment: donation, salary, bribe
    #frequency = Integer
    

