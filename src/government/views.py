from government.serializers import BillSerializer, PersonBillSerializer, LegalCaseSerializer, InstitutionSerializer
from government.models import Bill, PersonBill, LegalCase, Institution
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from utils.viewmixins import CreateOwnerMixin



"""

Viewsets

"""

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'uuid'


class LegalCaseViewSet(viewsets.ModelViewSet):
    queryset = LegalCase.objects.all()
    serializer_class = LegalCaseSerializer
    lookup_field = 'uuid'


class PersonBillViewSet(viewsets.ModelViewSet):
    queryset = PersonBill.objects.all()
    serializer_class = PersonBillSerializer
    lookup_field = 'uuid'

class InstitutionViewSet(CreateOwnerMixin, viewsets.ModelViewSet):
    
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    lookup_field = 'uuid'

    def create(self, request):
        return self.add_ownership(request=request, serializer_class=self.serializer_class)


"""

Views for Bill


class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'uuid'
    


class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'uuid'



Views for PersonBill


class PersonBillList(generics.ListCreateAPIView):
    queryset = PersonBill.objects.all()
    serializer_class = PersonBillSerializer
    lookup_field = 'uuid'

class PersonBillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonBill.objects.all()
    serializer_class = PersonBillSerializer
    lookup_field = 'uuid'


Views for LegalCase


class LegalCaseList(generics.ListCreateAPIView):
    queryset = LegalCase.objects.all()
    serializer_class = LegalCaseSerializer
    lookup_field = 'uuid'

class LegalCaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalCase.objects.all()
    serializer_class = LegalCaseSerializer
    lookup_field = 'uuid'

"""