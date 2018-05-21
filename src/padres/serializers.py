from rest_framework import serializers
from .models import Person, Promise



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = ('name', 'birthday', 'gender', 'uuid', 'long_description', 'owner', 'short_description')

class PromiseSerializer(serializers.ModelSerializer):
    people = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='get_delete_update_person',
        queryset=Person.objects.all()
    )
    class Meta:
        model = Promise
        fields = ('title', 'uuid', 'people', 'long_description')