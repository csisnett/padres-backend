from django.db import models
from utils.mixins import UUIDable, Descriptionable

class Genderable(models.Model):
    GENDER_CHOICES = (
    ('M', "Hombre"),
    ('F', 'Mujer'),
    ('O', 'Otro'),
    )
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)

    class Meta:
        abstract = True




class Event(Descriptionable, UUIDable, models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    date = models.DateField(default='0001-01-01', blank=True)
    people = models.ManyToManyField('Person', related_name='events')
    sources = models.ManyToManyField('Source')

class Scandal(UUIDable, Descriptionable, models.Model):

    events = models.ManyToManyField('Event')
    title = models.CharField(max_length=140, blank=True)


class Promise(Descriptionable, UUIDable, models.Model):
    PROMISE_CHOICES = (
    ('P', "Incumplida deliberadamente"),
    ('N', 'Incumplida por inacción'),
    ('H', 'Incumplida en parte'),
    ('M', 'Cumplida en su mayoría'),
    ('A', 'Cumplida completamente')
    )

    title = models.CharField(max_length=140)
    people = models.ManyToManyField('padres.Person', related_name='promises')
    events = models.ManyToManyField('padres.Event')
    category = models.CharField(max_length=3, choices=PROMISE_CHOICES, default='N')
    information = models.OneToOneField('StatementInformation', on_delete='CASCADE')


class Person(Contactable, Descriptionable, UUIDable, Genderable, models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=140)
    nickname = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(blank=True, null=True)
    #picture = models.ImageField()
    #jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    ownership = models.OneToOneField('transactions.Owner', on_delete='PROTECT', blank=True)
    short_description = models.CharField(max_length=140, blank=True)
    family = models.ManyToManyField('Person', blank=True)
    scandals = models.ManyToManyField('Scandal', related_name='people', blank=True)
    

class PoliticalParty(Contactable, Descriptionable, UUIDable, models.Model):
    name = models.CharField(max_length=140)
    people = models.ManyToManyField('Person', blank=True, related_name='party')

class Statement(Descriptionable, UUIDable, models.Model):
    STATEMENT_CHOICES = (
    ('LC', "Mentira Factual"),
    ('LO', 'Mentira por Omisión'),
    ('LF', 'Mentira por Influencia'),
    ('T', "Es Cierto"),
    ('UN', "No Verificado"),
    ('O', "Opinión")

    )

    title = models.CharField(max_length=140)
    people = models.ManyToManyField('padres.Person', related_name='statements')
    about_events = models.ManyToManyField('Event', blank=True) #if the statement is about an event
    category = models.CharField(max_length=3, choices=STATEMENT_CHOICES, default='UN')
    information = models.OneToOneField('StatementInformation', on_delete='CASCADE', related_name='statement')


class Believe(Descriptionable, UUIDable, models.Model):
    BELIEVE_CHOICES = (
    ('H', "Mantiene esta creencia"),
    ('C', 'Cambió  completamente'),
    ('P', 'Cambió en parte'),
    )

    title = models.CharField(max_length=140)
    people = models.ManyToManyField('padres.Person', related_name='believes')
    category = models.CharField(max_length=3, choices=BELIEVE_CHOICES, default='H')
    information = models.OneToOneField('StatementInformation', on_delete='CASCADE')

class Source(UUIDable, models.Model):
    url = models.URLField()
    published_date = models.DateField(default='0001-01-01', blank=True)

class Contactable(models.Model):
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    email_address = models.CharField(max_length=130, blank=True)
    website = models.URLField(blank=True)
    office_number = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True

class StatementInformation(UUIDable, models.Model):

    exact_statement = models.TextField()
    evidence = models.ManyToManyField('padres.Event', blank=True) #list of events that verify or not the statement
    date = models.DateField(default='0001-01-01', blank=True)