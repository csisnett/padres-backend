from django.db import models
import uuid as uuid_lib

class Institution(models.Model):
    pass

class Photo(models.Model):
    pass

class Event(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField()
    date = models.DateField()
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)


class Scandal(models.Model):
    pass

class Promise(models.Model):
    person = models.ManyToManyField('Person')
    title = models.CharField(max_length=140, blank=True, null=True)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)
    description = models.TextField()

class Transaction(models.Model):
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField()

class Company(models.Model):
    title = models.CharField(max_length=130)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)
    description = models.TextField()

class Contract(models.Model):
    title = models.CharField(max_length=140)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    description = models.TextField()


class Law_disorder(models.Model):
    pass


class Job(models.Model):
    """
    Job Model
    Defines the attributes of a job a person has/had
    for a period of time.
    """
    name = models.CharField(max_length=130)
    initial_date = models.DateField()
    termination_date = models.DateField()
    person = models.ManyToManyField('Person')
    actions = models.ManyToManyField(Event, related_name='actions')
    pay = models.IntegerField(null=True)
    #benefits = Insert
    law_events = models.ManyToManyField(Law_disorder)
    events = models.ManyToManyField(Event)
    description = models.TextField()

    #wasted_money = ...
    #law_disorder = ...
    #institution = ...
    #wasted_money = ... models.ManyToManyField(Transaction)s

class Person(models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=140)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    #picture = models.ImageField()
    jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    def __repr__(self):
        return self.name + ' is added.'
        
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

class CongressJob(models.Model):
    """
    Model for the job of being a congress man/woman.
    Defines the attributes, relations and methods of work in congress

    a congress job is CongressJob()
    """

    title = models.CharField(max_length=140)

    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    votes = models.ManyToManyField(Bill)


class Bill(models.Model):
    pass

    