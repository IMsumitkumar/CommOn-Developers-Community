from django.contrib import admin
from .models import MessageModel, News

admin.site.register(MessageModel)
admin.site.register(News)