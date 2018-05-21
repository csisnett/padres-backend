from rest_framework import serializers
from transactions.models import Company, BankAccount, Thing, Owner, Contract, Payment




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'ownership', 'owners', 'long_description', 'uuid')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('title', 'long_description', 'uuid', 'approved_by', 'companies')

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('balance', 'owners')

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ('name', 'owners', 'long_description', 'uuid')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('sender', 'receiver', 'amount', 'authorized_by', 'event', 'uuid')