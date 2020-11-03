from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CreateGroup(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    group_name = models.SlugField(max_length=200)
    description = models.CharField(max_length=250)
    

    def __str__(self):
        return self.group_name