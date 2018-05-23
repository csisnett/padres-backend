from rest_framework import serializers
from .models import CongressJob, GovernmentJob, PrivateJob, Institution

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

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'uuid', 'long_description')