from rest_framework import serializers
from government.models import Bill, PersonBill, LegalCase

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Bill
        fields = ('people', 'title', 'content',
         'status','uuid', 'long_description','short_description')
