from django.db import models

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
    pass

class Company(models.Model):
    name = models.CharField(max_length=170)

    def get_name(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=100)
    company = models.OneToOneField(Company)

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_company_name(self):
        return self.company.get_name()

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
    pay = models.IntegerField()
    benefits = models.ManyToManyField(Event, related_name='benefits')
    institution = models.ForeignKey(Institution)
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
    jobs = models.ForeignKey(Job, related_name='jobs')

    def get_gender(self):
        return self.gender
            
    def __repr__(self):
        return self.name + ' is added.'
        




    
