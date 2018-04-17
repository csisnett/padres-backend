from government.serializers import Bill, PersonBill, LegalCase
from rest_framework import generics

"""
Views for Bill
"""

class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'uuid'
    


class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'


"""
Views for PersonBill
"""

class PersonBillList(generics.ListCreateAPIView):
    queryset = PersonBill.objects.all()
    serializer_class = PersonBillSerializer
    lookup_field = 'uuid'

class PersonBillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonBill.objects.all()
    serializer_class = PersonBillSerializer
    lookup_field = 'uuid'

"""
Views for LegalCase
"""

class LegalCaseList(generics.ListCreateAPIView):
    queryset = LegalCase.objects.all()
    serializer_class = LegalCaseSerializer
    lookup_field = 'uuid'

class LegalCaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalCase.objects.all()
    serializer_class = LegalCaseSerializer
    lookup_field = 'uuid'
