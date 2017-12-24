from django.test import TestCase
from padres.models import Person, Job, Contract, Company


class ContractTest(TestCase):
    """Test module for contracts """

    def setUp(self):
        company1 = Company.objects.create(name="Toledano")
        company2 = Company.objects.create(name="Melo")
        Contract.objects.create(name="Tonosi",company = company1)
        Contract.objects.create(name="Pollos", company = company2)

    def test_contract_name(self):
        for Name in ("Tonosi", 'Pollos'):
            contract_for_test = Contract.objects.get(name=Name)
            self.assertEqual(contract_for_test.get_name(), Name)


    def test_company_name(self):
        for contract_name, company_name in zip(["Tonosi", "Pollos"],
        ["Toledano", "Melo"]):
            contract = Contract.objects.get(name=contract_name)
            self.assertEqual(contract.get_company().get_name(), company_name)


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
            person_zulay.get_gender(), "female")
        self.assertEqual(
            person_pedro.get_gender(), "male")

"""
maybe some day in the future I'll use this.
class MyTestsMeta(type):
    def __new__(cls, name, bases, attrs):
        for test_name in ({'compani': 'Toledan1o'}):
            attrs['test_%s' % test_name] = cls.gen(test_name)
        return super(MyTestsMeta, cls).__new__(cls, name, bases, attrs)

        @classmethod
        def gen(cls, test_name):
            #Returns a testcase that tests ``test_name``
            def fn(self):
                self.assertEqual(test(self.compani),"Toledano")
            return fn

class MyTests(TestCase):
    __metaclass__ = MyTestsMeta

"""