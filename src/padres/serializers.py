from rest_framework import serializers
from .models import (Person, Promise, Event,
 Scandal, Source, Statement, StatementInformation, PoliticalParty,
 Believe)



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = ('name', 'birthday', 'gender', 'ownership', 'short_description',
          'nickname', 'family', 'scandals', 'uuid',
         'long_description' 'twitter', 'facebook',
           'instagram', 'email_address', 'website', 'office_number')

class PromiseSerializer(serializers.ModelSerializer):
    people = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='person-detail',
        queryset=Person.objects.all(),
        lookup_field='uuid'
    )
    class Meta:
        model = Promise
        fields = ('title', 'uuid', 'events', 'category', 'information',
         'long_description', 'people')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Event
        fields = ('title', 'date', 'people', 'uuid', 'long_description', 'sources')

class ScandalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Scandal
        fields = ('events', 'title', 'people', 'uuid', 'long_description')

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Source
        fields = ('url', 'published_date', 'uuid')

class PoliticalPartySerializer(serializers.ModelSerializer):
    class Meta:

        model = PoliticalParty
        fields = ('name','people', 'uuid',
         'long_description' 'twitter', 'facebook',
           'instagram', 'email_address', 'website', 'office_number')

class BelieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Believe
        fields = ('title', 'people', 'category', 'information', 'long_description',
        'uuid')

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Statement
        fields = ('title', 'people', 'category', 'information', 'about_events',
        'long_description','uuid')

class StatementInformation(serializers.ModelSerializer):
    class Meta:
        model  = StatementInformation
        fields = ('exact_statement', 'evidence', 'date',
        'uuid')
