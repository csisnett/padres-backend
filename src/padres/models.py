from django.db import models
from utils.mixins import UUIDable, Descriptionable

class Genderable(models.Model):
    GENDER_CHOICES = (
    ('M', "Hombre"),
    ('F', 'Mujer'),
    )
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)

    class Meta:
        abstract = True


class Event(Descriptionable, UUIDable, models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    date = models.DateField(default='0001-01-01', blank=True)
    people = models.ManyToManyField('Person')

class Scandal(UUIDable, Descriptionable, models.Model):
    events = models.ManyToManyField('Event')
    short_description= models.CharField(max_length=140, blank=True)


class Promise(Descriptionable, UUIDable, models.Model):
    people = models.ManyToManyField('Person')
    title = models.CharField(max_length=140, blank=False, null=True)

class Person(Descriptionable, UUIDable, Genderable, models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=140)
    birthday = models.DateField(blank=True)
    #picture = models.ImageField()
    #jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    owner = models.OneToOneField('transactions.Owner', on_delete='PROTECT', blank=True, null=True)
    short_description = models.CharField(max_length=140, blank=True)