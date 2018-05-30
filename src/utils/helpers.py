from django.db import models
import uuid as uuid_lib
from django.apps import apps

def create_owner():
    Owner = apps.get_model('transactions' ,'Owner')
    owner = Owner()
    owner.save()
    return owner

def create_statement_information():
    StatementInformation = apps.get_model('padres', 'StatementInformation')
    statement = StatementInformation()
    statement.save()
    return statement