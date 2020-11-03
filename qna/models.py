from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Question(models.Model):

    asker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ques = models.CharField(max_length=250)

    def __str__(self):
        return self.ques[:30]

    class Meta:
        ordering = ['id']

class Answer(models.Model):

    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    teller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ans = models.CharField(max_length=250)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.ans[:10]
