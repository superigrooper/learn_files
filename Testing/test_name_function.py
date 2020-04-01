import unittest # модуль для тестирования
from get_name import get_formated_name

# этот класс содержит серию модульных тестов
class NamesTestCase(unittest.TestCase):
    """Тесты для 'get_name.py'"""

    # метод тестирует один аспект - правильность работы с двумя именами
    def test_first_last_name(self):
        """Имена вида Janis Joplin работают правильно?"""
        formatted_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    # тестирование работы ст ремя именами
    def test_first_middle_last_name(self):
        """Именя вида Ludqig Van Bethoven работают правильно?"""
        formatted_name = get_formated_name('ludvig', 'bethoven', 'van')
        self.assertEqual(formatted_name, 'Ludvig Van Bethoven')

if __name__ == '__main__':
    unittest.main()
