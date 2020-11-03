from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Project(models.Model):
    status = (
        ('STUCK', 'STUCK'),
        ('WORKING', 'WORKING'),
        ('DONE', 'DONE'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField('shortcut', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(User,related_name='project_teammates', blank=True)
    status = models.CharField(max_length=7, choices=status, default='STUCK')
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)
    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Task(models.Model):
    due = (
        ('PENDING', 'PENDING'),
        ('URGENT', 'URGENT'),
        ('DONE', 'DONE'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=80)
    due = models.CharField(max_length=7, choices=due, default='PENDING')
    body = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)
