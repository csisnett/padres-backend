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

"""Person Tests"""


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


class CreateNewPersonTest(TestCase):
    """Test module for inserting (POST) a new Person"""

    def setUp(self):
        diputado = Job.objects.create(name='Diputado', initial_date='2019-12-20',
         termination_date='2024-12-21')
        empresario = Job.objects.create(name='Business man', initial_date='2019-12-01',
        termination_date='2100-12-1')
        self.valid_person = {
            'name': 'Carlos',
            'birthday': '1996-06-19',
            'gender': 'male',
            'jobs': diputado.pk
        }

        self.invalid_person = {
            'name': '',
            'birthday': '1910-04-12',
            'gender': 'male',
            'jobs': empresario.pk
        }

    def test_create_valid_person(self):
        response = client.post(
            reverse('get_post_people'),
            data=json.dumps(self.valid_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_person(self):
        response = client.post(
            reverse('get_post_people'),
            data=json.dumps(self.invalid_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePersonTest(TestCase):
    """ Test module for updating an existing person record """

    def setUp(self):
        self.programmer = Job.objects.create(
            name='programmer', initial_date='1999-11-30', termination_date='2001-12-05')
        self.casper = Person.objects.create(
            name='casper', birthday='1898-05-11', gender='male', jobs=self.programmer)
        self.crispy = Person.objects.create(
            name='Krispy', birthday='1999-12-31', gender='female', jobs=self.programmer)
        self.mecanico = Job.objects.create(
        name='Mecanico', initial_date='1914-07-11', termination_date='1920-09-08')

        self.valid_payload = {
            'name': 'casper',
            'birthday': '1898-05-11',
            'gender': 'female',
            'jobs': self.mecanico.pk
        }
        self.invalid_payload = {
            'name': '',
            'birthday': '',
            'gender': 'female',
            'jobs': self.programmer.pk
        }

    def test_update_invalid_person(self):
        response = client.put(
            reverse('get_delete_update_person', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_person(self):
        response = client.put(
            reverse('get_delete_update_person', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePersonTest(TestCase):
    """Test module for deleting an existing person record"""

    def setUp(self):
        self.programmer = Job.objects.create(
            name='programmer', initial_date='1999-11-30', termination_date='2001-12-05')
        self.casper = Person.objects.create(
            name='casper', birthday='1898-05-11', gender='male', jobs=self.programmer)
        self.crispy = Person.objects.create(
            name='Krispy', birthday='1999-12-31', gender='female', jobs=self.programmer)
    
    def test_delete_valid_person(self):
        response = client.delete(
            reverse('get_delete_update_person', kwargs={'pk': self.casper.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_person(self):
        response = client.delete(
            reverse('get_delete_update_person', kwargs={'pk': 39}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


""" Contract Tests"""


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


class GetAllContractsTest(TestCase):
    
    def setUp(self):
        Odebretch = Company.objects.create(name='Odebretch')
        self.CintaCostera = Contract.objects.create(name='Cinta Costera 3', company=Odebretch)

    def test_get_all_contracts(self):
        response = client.get(
            reverse('get_post_contracts')
        )
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewContractTest(TestCase):
    """Test module for creating a new contract"""
    def setUp(self):
        self.oreo = Company.objects.create(name='Oreo')
        self.valid_contract = {
            'name': 'Muffin',
            'company': self.oreo.pk
        }
        self.invalid_contract = {
            'name': 'Pascual',
            'company': ''
        }

    def test_create_valid_contract(self):
        response = client.post(
            reverse('get_post_contracts'),
            data=json.dumps(self.valid_contract),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_contract(self):
        response = client.post(
            reverse('get_post_contracts'),
            data=json.dumps(self.invalid_contract),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleContractTest(TestCase):
    """Test module for updating a contract"""

    def setUp(self):
        self.ribasmith = Company.objects.create(
            name='Ribasmith')
        self.pollos = Contract.objects.create(
            name='Ribasmith Pollos contrato', company=self.ribasmith)
        self.valid_payload = {
            'name': 'Contrato de Pollos',
            'company': self.ribasmith.pk
        }
        self.invalid_payload = {
            'name': 'Contrato de carretera',
            'company': ''
        }
    def test_update_valid_contract(self):
        response = client.put(
            reverse('get_delete_update_contract', kwargs={'pk': self.pollos.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
    def test_update_invalid_contract(self):
        response = client.put(
            reverse('get_delete_update_contract', kwargs={'pk': self.pollos.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleContractTest(TestCase):
    """Test module for deleting an existing Person record """

    def setUp(self):
        self.ribasmith = Company.objects.create(
            name='Ribasmith')
        self.pollos = Contract.objects.create(
            name='Ribasmith Pollos contrato', company=self.ribasmith)

    def test_delete_valid_contract(self):
        response = client.delete(
            reverse('get_delete_update_contract', kwargs={'pk': self.pollos.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_contract(self):
        response = client.delete(
            reverse('get_delete_update_contract', kwargs={'pk': 19}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
""" Job Tests """

class GetAllJobsTest(TestCase):
    """Test module for GET all jobs API"""

    def setUp(self):
        self.programmer = Job.objects.create(
            name='programmer', initial_date='1999-11-30', termination_date='2001-12-05')
    def test_get_all_jobs(self):
        #get API response
        response = client.get(reverse('get_post_jobs'))
        #get data from db
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleJobTest(TestCase):
    "Test module for GET single job API"

    def setUp(self):
        self.mecanico = Job.objects.create(
        name='Mecanico', initial_date='1914-07-11', termination_date='1920-09-08')

    def test_get_valid_single_job(self):
        response = client.get(
            reverse('get_delete_update_job', kwargs={'pk': self.mecanico.pk}))
        job = Job.objects.get(pk=self.mecanico.pk)
        serializer = JobSerializer(job)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_job(self):
        response = client.get(
            reverse('get_delete_update_job', kwargs={'pk': 25})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewJobTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'Mecanico',
            'initial_date': '1010-12-31',
            'termination_date': '1904-06-15'
        }
        self.invalid_payload = {
            'name': 'Diputado',
            'initial_date': '',
            'termination_date': ''
        }

    def test_create_valid_job(self):
        response = client.post(
            reverse('get_post_jobs'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_invalid_job(self):
        response = client.post(
            reverse('get_post_jobs'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

""" Company Tests"""

class GetSingleCompanyTest(TestCase):


    def setUp(self):
        self.apple = Company.objects.create(name='Apple Computer')
        self.hola = Company.objects.create(name='HOLA')

    def test_get_valid_single_company(self):
        response = client.get(
            reverse('get_delete_update_company',kwargs={'pk': self.apple.pk}))

        company = Company.objects.get(pk=self.apple.pk)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_company(self):
        response = client.get(
            reverse('get_delete_update_company',kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetAllCompaniesTest(TestCase):


    def setUp(self):
        self.firstcompany = Company.objects.create(name='First')
        self.two = Company.objects.create(name='Second')

    def test_get_all_companies(self):
        response = client.get(reverse('get_post_companies'))
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewCompanyTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'name'
        }
        self.invalid_payload = {
            'name': ''
        }

    def test_create_valid_company(self):
        response = client.post(
            reverse('get_post_companies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        response = client.post(
            reverse('get_post_companies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

