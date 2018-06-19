from rest_framework import serializers
from .models import CongressJob, GovernmentJob, PrivateJob

class CongressJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongressJob
        fields = ('title', 'uuid', 'long_description')

class GovernmentJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentJob
        fields = ('title', 'uuid', 'long_description', 'institution')

class PrivateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateJob
        fields = ('title', 'uuid', 'long_description', 'company')