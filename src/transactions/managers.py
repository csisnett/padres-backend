from django.db import models
import uuid as uuid_lib
from django.apps import apps

class CompanyManager(models.Manager):

    def create_object(self, name, long_description=''):
        Owner = apps.get_model('transactions' ,'Owner')
        owner = Owner()
        owner.save()
        company = self.model(name=name,
                            ownership=owner,
                            uuid=uuid_lib.uuid4(),
                            long_description=long_description)

        company.save()
        return company