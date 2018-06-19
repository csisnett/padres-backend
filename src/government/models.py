from django.db import models
from utils.mixins import UUIDable, Descriptionable


class Institution(Descriptionable, UUIDable, models.Model):
    name = models.CharField(max_length=130)
    events_list = models.ManyToManyField('padres.ListOfEvent')
    events = models.ManyToManyField('padres.Event')


class Bill(UUIDable, Descriptionable, models.Model):
    """
    Model for a bill or anything that congress or people can vote on.
    Defines the attributes, relations of a bill.
    

    """

    people = models.ManyToManyField('padres.Person', through='PersonBill')
    
    title = models.CharField(max_length=140)
    short_description = models.CharField(max_length=300)
    content = models.TextField()
    status = models.CharField(max_length=40)
    

class PersonBill(UUIDable, models.Model):
    """
    intermediary table/model between a Person and a Bill

    Defines the attributes, and methods of the relationship.
    """
    VOTE_CHOICES = (
        ('y', 'vote of approval'),
        ('n', 'rejection vote'),
        ('a', 'absent from session'),
        ('r', 'refused to vote'),
    )
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)
    reason = models.TextField()
    person = models.ForeignKey('padres.Person', on_delete='CASCADE')
    bill = models.ForeignKey(Bill, on_delete='CASCADE')

class LegalCase(UUIDable, Descriptionable, models.Model):
    """
    Legal Case Model
    Defines the attributes and relations of a legal case

    case is  Legal_Case(String, String ... Persons' UUID, Event's UUID)

    interpretation: a Legal Case with a UUID, title, description, many-to-many to Person,
    and many-to-many to Event relationships

    example:
    case-1 = Legal_Case(
        title='Tonosi',
        description='Awful',
        Person=UUID, UUID,
        Events=UUID, UUID,
    )

    """

    title = models.CharField(max_length=140)
    people = models.ManyToManyField('padres.Person', blank=True)
    events = models.ManyToManyField('padres.Event', blank=True)
    short_description = models.CharField(max_length=300)