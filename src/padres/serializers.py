from rest_framework import serializers
from .models import Person, Promise, Event, Scandal, Resource



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = ('name', 'birthday', 'gender', 'uuid',
         'long_description', 'ownership', 'short_description',
          'nickname', 'family', 'scandals')

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

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Event
        fields = ('title', 'date', 'people', 'uuid', 'long_description', 'resources')

class ScandalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Scandal
        fields = ('events', 'short_description', 'people', 'uuid', 'long_description')

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Resource
        fields = ('url', 'published_date', 'uuid')