import unittest
from city import city

class CityTestInfo(unittest.TestCase):
    """Тесты для 'city.py'"""

    def test_city_info_2args(self):
        """Проверка работы с двумя аргументами"""
        info = city('moscow', 'russia')
        self.assertEqual(info, 'Moscow Russia')

    def test_city_info_3args(self):
        """Проверка работы с тремя аргументами"""
        info = city('moscow', 'russia', 15000000)
        self.assertEqual(info, 'Moscow Russia, population: 15000000')

if __name__ == '__main__':
    unittest.main()