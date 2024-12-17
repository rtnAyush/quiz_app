from django.db import models

# Create your models here.
class QuizSession(models.Model):
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return 'Total question attempted' + self.total_questions

