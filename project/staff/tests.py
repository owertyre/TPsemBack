from django.test import TestCase
from models import Staff
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        Staff.objects.create(
            name='Тестов Тест Тестович',
            companyName='ООО тест',
            positionName='Тестировщик',
            hireDate='10.01.2023',
            fireDate='11.01.2023',
            salary=100000,
            fraction=100000,
            base=100000,
            advance=100000,
            byHours=False)


    def test_correctness_types(self):
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").name, str)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").companyName, str)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").positionName, str)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").hireDate, str)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").fireDate, str)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").salary, int)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").fraction, int)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").base, int)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").advance, int)
        self.assertIsInstance(Staff.objects.get(name="Тестов Тест Тестович").byHours, bool)

    def test_correctness_data(self):
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").name == 'Тестов Тест Тестович')
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").companyName == 'ООО тест')
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").positionName == 'Тестировщик')
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").hireDate == '10.01.2023')
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").fireDate == '11.01.2023')
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").salary == 100000)
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").fraction == 100000)
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").base == 100000)
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").advance == 100000)
        self.assertTrue(Staff.objects.get(name="Тестов Тест Тестович").byHours == False)
