from rest_framework import serializers
from .models import Bill, PersonBill, LegalCase

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Bill
        fields = ('people', 'title', 'content',
         'status','uuid', 'long_description','short_description')

class LegalCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model  = LegalCase
        fields = ('people', 'title', 'events',
         'uuid', 'long_description','short_description')


class PersonBillSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PersonBill
        fields = ('uuid', 'vote' 'reason', 'person', 'bill')