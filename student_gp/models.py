from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models
from django.conf import settings
import uuid
from taggit.managers import TaggableManager
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField

class DateTimeModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MessageModel(DateTimeModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Group, verbose_name="room_name", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'sender', on_delete=models.CASCADE, null=True)
    message = models.TextField('body')
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recipients')

    def __unicode__(self):
        return self.id

    def __str__(self):
        return f'{self.message} sent by {self.user} in Room {self.room}'

    class Meta:
        ordering = ['-id']


class News(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    image = ResizedImageField(size=[500, 500],upload_to="news_post",null=True, blank=True)
    room_field = models.CharField(max_length=10, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title