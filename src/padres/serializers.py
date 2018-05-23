from rest_framework import serializers
from .models import Person, Promise, Event, Scandal



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = ('name', 'birthday', 'gender', 'uuid', 'long_description', 'owner', 'short_description')

class PromiseSerializer(serializers.ModelSerializer):
    people = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='person-detail',
        queryset=Person.objects.all(),
        lookup_field='uuid'
    )
    class Meta:
        model = Promise
        fields = ('title', 'uuid', 'long_description', 'people')