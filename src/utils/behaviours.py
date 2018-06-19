from django.db import models

class Contactable(models.Model):
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    email_address = models.CharField(max_length=130, blank=True)
    website = models.Field(blank=True)
    office_number = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True

class Updatable(models.Model):
    last_modification = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField(auto_now_add=True) #date it was first uploaded to Padres

    class Meta:
        abstract = True

    