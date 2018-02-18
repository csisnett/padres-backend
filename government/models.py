from django.db import models

class Bill(models.Model):
    """
    Model for a bill or anything that congress or people can vote on.
    Defines the attributes, relations of a bill.
    

    """
    person = models.ManyToManyField(Person, through='PersonBill')
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    exact_text = models.TextField()
    status = models.CharField(max_length=40)
    #state = 

class PersonBill(models.Model):
    """
    intermediary table/model between a Person and a Bill

    Defines the attributes, and methods of the relationship.
    """
    VOTE_CHOICES = (
        ('b', "Bill hasn't come to vote"),
        ('y', 'yes'),
        ('n', 'no'),
        ('a', 'absent from session'),
        ('r', 'refused to vote'),
    )
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)
    reason_for_vote = models.TextField()

class LegalCase(models.Model):
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
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    title = models.CharField(max_length=140)
    description = models.TextField()
    person = models.ManyToManyField(Person)
    Event = models.ManyToManyField(Event)