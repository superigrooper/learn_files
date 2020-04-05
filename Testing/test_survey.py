import unittest
from survey import AnonymosSurvey

class TestAnonymosSurvey(unittest.TestCase):
    """Тесты для класса AnonymosSurvey"""

    # при наличии метода setUp() интерпретатор перед каждым запуском метода
    # начинающегося с test_ запускает метод setUp() для создания данных для теста
    def setUp(self):
        """
        Содание опроса и ответов для всех тестовых методов
        """
        question = "Какую операционную систему предпочитаете?"
        self.my_survey = AnonymosSurvey(question)
        self.responses = ['windows', 'linux', 'mac']

    def test_store_single_responses(self):
        """Тест метода сохранения ответов"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Тест метода сохранения нескольких ответов."""
        for res in self.responses:
            self.my_survey.store_responses(res)

        for res in self.responses:
            self.assertIn(res, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()