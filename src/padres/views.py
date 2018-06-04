from padres.models import (Person, Promise, Event, Scandal,
 Source, Statement, StatementInformation, Believe, PoliticalParty)

from padres.serializers import (PersonSerializer, PromiseSerializer, ScandalSerializer,
EventSerializer, SourceSerializer, BelieveSerializer, StatementInformationSerializer,
 StatementSerializer, PoliticalPartySerializer)

from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from utils.viewmixins import CreateOwnerMixin, CreateStatementInfoMixin

"""
Viewsets
"""

class PersonViewSet(CreateOwnerMixin, viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'

    def create(self, request):
        return self.add_ownership(request=request, serializer_class=self.serializer_class)

class PromiseViewSet(viewsets.ModelViewSet):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    lookup_field = 'uuid'

    def create(self, request):
        return self.add_statement_information(request=request, serializer_class=self.serializer_class)

class ScandalViewSet(viewsets.ModelViewSet):
    queryset = Scandal.objects.all()
    serializer_class = ScandalSerializer
    lookup_field = 'uuid'


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'uuid'


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'uuid'

class BelieveViewSet(viewsets.ModelViewSet):
    queryset = Believe.objects.all()
    serializer_class = BelieveSerializer
    lookup_field = 'uuid'

    def create(self, request):
        return self.add_statement_information(request=request, serializer_class=self.serializer_class)


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    lookup_field = 'uuid'

    def create(self, request):
        return self.add_statement_information(request=request, serializer_class=self.serializer_class)


class StatementInformationViewSet(viewsets.ModelViewSet):
    queryset = StatementInformation.objects.all()
    serializer_class = StatementInformationSerializer
    lookup_field = 'uuid'

class PoliticalPartyViewSet(viewsets.ModelViewSet):
    queryset = PoliticalParty.objects.all()
    serializer_class = PoliticalPartySerializer
    lookup_field = 'uuid'

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'uuid'


"""
Just in case

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'

"""

"""
Views for Promise
"""
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
"""
Views for Scandal
"""
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

"""
Views for Event
"""
"""
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'uuid'


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'uuid'




Views for Resource


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'uuid'


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'uuid'

    """