from django.db import models
import uuid as uuid_lib

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

class Person(models.Model):
    """
    Person Model
    Defines the attributes of a person
    """
    name = models.CharField(max_length=140)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    #picture = models.ImageField()
    #jobs = models.ForeignKey(Job, related_name='jobs',on_delete=models.PROTECT)
    uuid = models.UUIDField(
    db_index=True,
    default=uuid_lib.uuid4,
    editable=False)

    def __repr__(self):
        return self.name + ' is added.'
        


