from django.db import models
from auth_system.models import *
# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return f'Питання #{self.pk}'

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['pk']

class Choice(models.Model):
    respond = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    def show_persent(self):
        number_answers = len(Answer.objects.filter(question=self.question).all())
        number_this_answers = len(Answer.objects.filter(choice=self).all())
        if number_answers == 0 or number_this_answers == 0:
            return 0
        percent = int((number_this_answers * 100) / number_answers)
        return percent

    def __str__(self):
        return f'Відповідь  до питання #{self.question.pk} - {self.respond}'

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers_q", null=True, blank="True")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Відповідь {self.user.username} до питання #{self.question.pk}'

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        unique_together = [["user", "question"]]