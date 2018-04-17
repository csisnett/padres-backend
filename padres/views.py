from padres.models import Person, Promise
from padres.serializers import PersonSerializer, PromiseSerializer
import pdb
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


"""
Views for Person
"""

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated, )


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
Old views for Contracts


"""