import unittest
from employee import Employee

class TestEmployeeMethods(unittest.TestCase):
    """Тестирование методов повышения оклада."""

    def setUp(self):
        """Создание модели работника для тестов.""" 
        self.my_employee = Employee('vitla', 'biostar', 10000)

    def test_raise_salary_default(self):
        """Тест метода со значением по умолчанию"""
        self.my_employee.raise_salary()
        self.assertEqual(15000, self.my_employee.salary)

    def test_raise_salary_custom(self):
        """Тест метода с пользовательским значением"""
        self.my_employee.raise_salary(3000)
        self.assertEqual(13000, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()