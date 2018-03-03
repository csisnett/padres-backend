from django.db import models
from utils.mixins import UUIDable, Descriptionable

class Genderable(models.Model):
    gender = models.ChoiceField()

class Photo(models.Model):
    pass

class Event(Descriptionable, UUIDable, models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    date = models.DateField()


class Scandal(models.Model):
    pass

class Promise(Descriptionable, UUIDable, models.Model):
    person = models.ManyToManyField('Person')
    title = models.CharField(max_length=140, blank=True, null=True)

class Person(Descriptionable, UUIDable, Genderable, models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=140)
    birthday = models.DateField()
    #picture = models.ImageField()
    #jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    owner = models.OneToOneField('transactions.Owner', on_delete='CASCADE')