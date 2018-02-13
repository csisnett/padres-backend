from rest_framework import serializers
from .models import Person, Job, Contract, Company, Transaction, Promise


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name', 'initial_date', 'termination_date')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = ('name', 'birthday', 'gender', 'jobs')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('name', 'company')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('name', 'uuid')

class PromiseSerializer(serializers.ModelSerializer):
    person = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='get_delete_update_person',
        queryset=Person.objects.all()
    )
    class Meta:
        model = Promise
        fields = ('name', 'uuid', 'person')