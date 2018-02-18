from django.db import models

class JobMixin(models.Model):
    """
    Job Model
    Defines the attributes of a job a person has/had
    for a period of time.
    """
    title = models.CharField(max_length=130)
    initial_date = models.DateField()
    termination_date = models.DateField()
    person = models.ManyToManyField('Person')
    pay = models.IntegerField(null=True)
    #benefits = Insert

    class Meta:
        abstract = True

    #wasted_money = ...
    #law_disorder = ...
    #institution = ...
    #wasted_money = ... models.ManyToManyField(Transaction)s


class CongressJob(models.Model):
    """
    Model for the job of being a congress man/woman.
    Defines the attributes, relations and methods of work in congress

    a congress job is CongressJob()
    """

    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)
    
    description = models.TextField()
    #absences


class Institution(models.Model):
    pass