from django.db import models
import uuid as uuid_lib

class Institution(models.Model):
    pass

class Photo(models.Model):
    pass

class Event(models.Model):
    pass

class Scandal(models.Model):
    pass

class Promise(models.Model):
    pass

class Transaction(models.Model):
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    name = models.CharField(max_length=140,
    blank=True,
    null=True)


class Company(models.Model):
    name = models.CharField(max_length=170)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    def get_name(self):
        return self.name
    def get_uuid(self):
        return self.uuid

class Contract(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    def get_name(self):
        return self.name
    def get_uuid(self):
        return self.uuid

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
    promises = models.ManyToManyField(Promise)
    pay = models.IntegerField(null=True)
    benefits = models.ManyToManyField(Event, related_name='benefits')
    institution = models.ForeignKey(Institution,on_delete=models.PROTECT)
    law_events = models.ManyToManyField(Law_disorder)
    events = models.ManyToManyField(Event)
    #benefits = ...#undefined
    #wasted_money = ...
    #law_disorder = ...
    institution = ...
    #wasted_money = ... models.ManyToManyField(Transaction)s

class Person(models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    #picture = models.ImageField()
    jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    def get_gender(self):
        return self.gender

    def get_uuid(self):
        return self.uuid
            
    def __repr__(self):
        return self.name + ' is added.'
        




    
