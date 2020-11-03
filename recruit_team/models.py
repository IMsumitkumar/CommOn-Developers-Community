from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class AskTeam(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    team_size = models.IntegerField()
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title
