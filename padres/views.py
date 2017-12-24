from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from padres.models import Person, Job, Contract, Company
from padres.serializers import PersonSerializer, JobSerializer, ContractSerializer, CompanySerializer

"""
Views for Person
"""

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single person
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    # delete a single person
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single person
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_people(request):
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        return Response({})

"""
Views for Job
"""

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single Job
    if request.method == 'GET':
        return Response({})
    # delete a single Job
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single Job
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_jobs(request):
    if request.method == 'GET':
        return Response({})

    elif request.method == 'POST':
        return Response({})


"""
Views for Contract
"""

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_contract(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single Contract
    if request.method == 'GET':
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    # delete a single Contract
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single Contract
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_contracts(request):
    if request.method == 'GET':
        return Response({})

    elif request.method == 'POST':
        return Response({})

"""
Views for Company
"""

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_company(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get details of a single Company
    if request.method == 'GET':
        return Response({})
    # delete a single Company
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single Company
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_companies(request):
    if request.method == 'GET':
        return Response({})

    elif request.method == 'POST':
        return Response({})