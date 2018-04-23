from django.db import models
from utils.mixins import UUIDable, Descriptionable

class Jobable(Descriptionable, UUIDable, models.Model):
    """
    Job Model
    Defines the attributes of a job a person has/had
    for a period of time.
    """
    title = models.CharField(max_length=130)
    initial_date = models.DateField()
    termination_date = models.DateField()
    pay = models.IntegerField(null=True)


    #benefits = Insert

    class Meta:
        abstract = True

    #wasted_money = ...
    #institution = ...
    #wasted_money = ... models.ManyToManyField(Transaction)s

class GovernmentJob(Jobable, models.Model):
    institution = models.ForeignKey('Institution', on_delete='PROTECT')

class CongressJob(Jobable, models.Model):
    pass

class PrivateJob(Jobable, models.Model):
    company = models.ForeignKey('transactions.Company', on_delete='PROTECT')

class Institution(Descriptionable, UUIDable, models.Model):
    name = models.CharField(max_length=130)