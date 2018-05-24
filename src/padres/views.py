from padres.models import Person, Promise, Event, Scandal, Resource
from padres.serializers import (PersonSerializer, PromiseSerializer, ScandalSerializer,
EventSerializer, ResourceSerializer)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


"""
Views for Person
"""

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'


"""
Views for Promise
"""

class PromiseList(generics.ListCreateAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    lookup_field = 'uuid'

class PromiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    lookup_field = 'uuid'


"""
Views for Scandal
"""

class ScandalList(generics.ListCreateAPIView):
    queryset = Scandal.objects.all()
    serializer_class = ScandalSerializer
    lookup_field = 'uuid'


class ScandalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scandal.objects.all()
    serializer_class = ScandalSerializer
    lookup_field = 'uuid'



"""
Views for Event
"""

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'uuid'


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'uuid'



"""
Views for Resource
"""

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'uuid'


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'uuid'