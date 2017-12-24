import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from padres.models import Person, Job, Contract, Company
from padres.serializers import (PersonSerializer, JobSerializer,
 CompanySerializer, ContractSerializer)
import pdb

#initialize the APIClient App
client = Client()

class GetAllPeopleTest(TestCase):
    """ Test module for GET all people API"""

    def setUp(self):
        webprogrammer = Job.objects.create(name="Programmer", initial_date="2014-07-01",
        termination_date="2019-07-01")
        diputado19 = Job.objects.create(name="Diputado", initial_date="2014-05-01",
        termination_date="2020-06-01")
        Person.objects.create(
            name='Carlos', birthday='1996-06-09', gender='male', jobs=webprogrammer)
        Person.objects.create(
            name='Ernesto', birthday='1976-06-10', gender='male', jobs=diputado19)
        Person.objects.create(
            name='Maria', birthday='1936-06-14', gender='female', jobs=diputado19)
        
    def test_get_all_people(self):
        #get API response
        response  = client.get(reverse('get_post_people'))
        #get data from db
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
class GetSinglePersonTest(TestCase):
     Test module for GET single person API

    def setUp(self):
        diputado14 =  Job.objects.create(name="Diputado", initial_date="2014-07-01",
        termination_date="2019-07-01")
        self.zulay = Person.objects.create(name='Zulay',birthday='1951-05-12',
        gender='female', jobs=diputado14)
        self.pedro = Person.objects.create(name="Pedro Miguel", birthday='1962-05-11',
        gender='male', jobs=diputado14)

    def test_get_valid_single_person(self):
        response = client.get(reverse('get_delete_update_person', kwargs={'pk': self.zulay.pk}))
        person = Person.objects.get(pk=self.zulay.pk)
        serializer = PersonSerializer(person)
        print(serializer.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_person(self):
        response = client.get(
            reverse('get_delete_update_person', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        """

class GetSinglePersonTest(TestCase):
    """ Test module for GET single Person API """

    def setUp(self):
        diputado19 = Job.objects.create(name="Diputado", initial_date="2014-07-01",
        termination_date="2019-07-01")
        self.pedro = Person.objects.create(name="Pedro Miguel", birthday='1960-05-11',
        gender='male', jobs=diputado19)

    def test_get_invalid_single_person(self):
        response = client.get(reverse('get_delete_update_person', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_single_person(self):
        response = client.get(
            reverse('get_delete_update_person', kwargs={'pk': self.pedro.pk}))
        person = Person.objects.get(pk=self.pedro.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleContractTest(TestCase):

    def setUp(self):
        Toledano = Company.objects.create(name='Toledano')
        self.palomilla = Contract.objects.create(name="Palomilla", company=Toledano)

    def test_get_valid_single_contract(self):
        response = client.get(
            reverse(
                'get_delete_update_contract', kwargs={'pk': self.palomilla.pk}))
        contract = Contract.objects.get(pk=self.palomilla.pk)
        serializer = ContractSerializer(contract)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_contract(self):
        response = client.get(reverse('get_delete_update_contract', kwargs={'pk': 121}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


