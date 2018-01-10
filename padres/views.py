from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from padres.models import Person, Job, Contract, Company
from padres.serializers import PersonSerializer, JobSerializer, ContractSerializer, CompanySerializer
import pdb
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
    
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'birthday': request.data.get('birthday'),
            'gender': request.data.get('gender'),
            'jobs': request.data.get('jobs')
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        serializer = JobSerializer(job)
        return Response(serializer.data)
    # delete a single Job
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single Job
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_jobs(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

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
    #get all contracts
    if request.method == 'GET':
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)

    #create a new contract
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'company': request.data.get('company')
        }
        serializer = ContractSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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