from django.db import models

class Institution(models.Model):
    pass

class Photo(models.Model):
    pass

class Event(models.Model):
    title = models.CharField(max_length=130)
    description = models.TextField(default='Event')
    date = models.DateField(default='0001-01-01')
    related_events = models.ManyToManyField('padres.Event')
    

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
    person = models.ManyToManyField('Person', through='padres.Gig')
    pay = models.IntegerField(default=0)
    benefits = models.ManyToManyField(Event, related_name='benefits')
    institution = models.ForeignKey(Institution,on_delete=models.PROTECT)
    events = models.ManyToManyField(Event)
    #benefits = ...#undefined
    #wasted_money = ...
    #law_disorder = ...
    #wasted_money = ... models.ManyToManyField(Transaction)s

    def __str__(self):
        return self.name

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

    def get_gender(self):
        return self.gender
            
    def __repr__(self):
        return self.name + ' is added.'

    def __str__(self):
        return self.name
        


class Gig(models.Model):
    initial_date = models.DateField()
    termination_date = models.DateField()
    persons_role = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)

