from utils.helpers import create_owner
from transactions.serializers import CompanySerializer
from rest_framework.response import Response 
from rest_framework import status


class CreateOwnerMixin:

    def add_ownership(self, request, serializer_class):
        editable_request = request.data.copy()
        editable_request.__setitem__('ownership', create_owner().pk)

        serializer = serializer_class(data=editable_request)
        if serializer.is_valid(self):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
