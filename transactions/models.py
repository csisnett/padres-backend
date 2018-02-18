from django.db import models

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
