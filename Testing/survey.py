class AnonymosSurvey():
    """Сбор анонимных ответов на вопросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.question)

    def store_responses(self, new_response):
        """Сохраняет новый вопрос."""
        self.responses.append(new_response)

    def show_responses(self):
        """Показывает ответы."""
        print("Список ответов:")
        for res in self.responses:
            print(f" - {res}")