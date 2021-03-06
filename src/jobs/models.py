from django.db import models
from utils.mixins import UUIDable, Descriptionable

class Jobable(Descriptionable, UUIDable, models.Model):
    """
    Job Model
    Defines the attributes of a job
    """
    title = models.CharField(max_length=130, unique=True)

    #benefits = Insert

    class Meta:
        abstract = True

    #wasted_money = ...
    #institution = ...
    #wasted_money = ... models.ManyToManyField(Transactions)
    

class GovernmentJob(Jobable, models.Model):
    institution = models.ForeignKey('government.Institution', on_delete='PROTECT')
    people = models.ManyToManyField('padres.Person', blank=True, through='Person_GovernmentJob')

class CongressJob(Jobable, models.Model):
    pass

class PrivateJob(Jobable, models.Model):
    company = models.ForeignKey('transactions.Company', on_delete='PROTECT', blank=True, null=True)
    people = models.ManyToManyField('padres.Person', blank=True, through='Person_PrivateJob')




class Person_GovernmentJob(models.Model):
    """
    intermediary table between person and governmentjob

    """
    person = models.ForeignKey('padres.Person', on_delete='CASCADE')
    government_job = models.ForeignKey(GovernmentJob, on_delete='CASCADE')
    initial_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)

class Person_PrivateJob(models.Model):
    """
    intermediary table between person and PrivateJob

    """
    person = models.ForeignKey('padres.Person', on_delete='CASCADE')
    government_job = models.ForeignKey(PrivateJob, on_delete='CASCADE')
    initial_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)