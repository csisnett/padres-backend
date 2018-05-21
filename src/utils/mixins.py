from django.db import models
import uuid as uuid_lib

class Descriptionable(models.Model):
    long_description = models.TextField(blank=True)

    class Meta:
        abstract = True

class UUIDable(models.Model):
    uuid = models.UUIDField(
    default=uuid_lib.uuid4,
    editable=False)

    class Meta:
        abstract = True

