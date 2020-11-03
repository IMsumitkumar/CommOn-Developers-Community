from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.contrib.auth.models import Group


# Create your models here.
class Profile(models.Model):
    COUNTRIES = [
            ('INDIA','INDIA'),
            ('USA', 'USA'),
            ('NEW YORK', 'NEW YORK'),
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=False, blank=False, null=True)
    profile_pic = ResizedImageField(size=[90, 90],default='profile.png',null=True, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    country = models.CharField(max_length=10,choices=COUNTRIES, blank=True, null=True
    )
    address = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class SelectGroups(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, default='',blank=True, null=True, unique=False, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Group'

