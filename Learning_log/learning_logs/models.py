from django.db import models

# Create your models here.
class Topic(models.Model):
    """Текущая тема."""
    text = models.CharField(max_length=200) # для небольшого объёма текста
    date_added = models.DateTimeField(auto_now_add=True) # присвоение даты

    def __str__(self):
        return self.text

class Entry(models.Model):
    """Изученная пользователем информация"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text