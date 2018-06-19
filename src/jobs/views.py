from jobs.models import CongressJob, GovernmentJob, PrivateJob
from jobs.serializers import GovernmentJobSerializer, CongressJobSerializer, PrivateJobSerializer
from rest_framework import viewsets
from utils.viewmixins import CreateOwnerMixin

"Viewsets"

class CongressJobViewSet(viewsets.ModelViewSet):
    """
    A viewset for congressjob
    """

    queryset = CongressJob.objects.all()
    serializer_class = CongressJobSerializer
    lookup_field = 'uuid'



class GovernmentJobViewSet(viewsets.ModelViewSet):
    
    queryset = GovernmentJob.objects.all()
    serializer_class = GovernmentJobSerializer
    lookup_field = 'uuid'


class PrivateJobViewSet(viewsets.ModelViewSet):
    
    queryset = PrivateJob.objects.all()
    serializer_class = PrivateJobSerializer
    lookup_field = 'uuid'

        

"""
class CongressJobList(generics.ListCreateAPIView):
    queryset = CongressJob.objects.all()
    serializer_class = CongressJobSerializer
    lookup_field = 'uuid'


class CongressJobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CongressJob.objects.all()
    serializer_class = CongressJobSerializer
    lookup_field = 'uuid'




class GovernmentJobList(generics.ListCreateAPIView):
    queryset = GovernmentJob.objects.all()
    serializer_class = GovernmentJobSerializer
    lookup_field = 'uuid'


class GovernmentJobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GovernmentJob.objects.all()
    serializer_class = GovernmentJobSerializer
    lookup_field = 'uuid'

class PrivateJobList(generics.ListCreateAPIView):
    queryset = PrivateJob.objects.all()
    serializer_class = PrivateJobSerializer
    lookup_field = 'uuid'


class PrivateJobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrivateJob.objects.all()
    serializer_class = PrivateJobSerializer
    lookup_field = 'uuid'

class InstitutionList(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    lookup_field = 'uuid'


class InstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    lookup_field = 'uuid'

    """