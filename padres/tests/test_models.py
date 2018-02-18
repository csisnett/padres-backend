from django.test import TestCase
from padres.models import Person, Job, Contract, Company

"""
class ContractTest(TestCase):
    "Test module for contracts "

    def setUp(self):
        c1 = Company.objects.create(name="Toledano")
        company2 = Company.objects.create(name="Melo")
        Contract.objects.create(name="Tonosi", company=c1)
        Contract.objects.create(name="Pollos", company=company2)

    def test_contract_name(self):
        contract1 = Contract.objects.get(name='Tonosi')
        contract2 = Contract.objects.get(name='Pollos')

        self.assertEqual(contract1.get_name(), "Tonosi")
        self.assertEqual(contract2.get_name(), "Pollos")


    def test_company_name(self):
        for contract_name, company_name in zip(["Tonosi", "Pollos"],
        ["Toledano", "Melo"]):
            contract = Contract.objects.get(name=contract_name)
            self.assertEqual(contract.get_company().get_name(), company_name)

"""
class PersonTest(TestCase):
    """Test module for Person model """

    def setUp(self):
        diputado19 = Job.objects.create(name="Diputado", initial_date="2014-07-01",
        termination_date="2019-07-01")

        Person.objects.create(name='Zulay',birthday='1950-05-12',
        gender='female', jobs=diputado19)

        Person.objects.create(name="Pedro Miguel", birthday='1960-05-11',
        gender='male', jobs=diputado19)

    def test_person_gender(self):
        person_zulay = Person.objects.get(name='Zulay')
        person_pedro = Person.objects.get(name='Pedro Miguel')

        self.assertEqual(
            person_zulay.gender, "female")
        self.assertEqual(
            person_pedro.gender, "male")


class TransactionTest(TestCase):
    
    def setUp(self):
        Contract.objects.create(name='numero 1')

    def test_contract_name(self):
        c1 = Contract.objects.get(name='numero 1')
        self.assertEqual(c1.name, "numero 1")