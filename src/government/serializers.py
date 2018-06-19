from rest_framework import serializers
from .models import Bill, PersonBill, LegalCase, Institution

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
        fields = ('uuid', 'vote', 'reason', 'person', 'bill')

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'uuid', 'long_description', 'events_list')