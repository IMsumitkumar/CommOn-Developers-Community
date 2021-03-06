# Generated by Django 3.1.3 on 2020-12-18 19:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[500, 500], upload_to='news_post')),
                ('room_field', models.CharField(blank=True, max_length=10)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(verbose_name='body')),
                ('recipients', models.ManyToManyField(related_name='recipients', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='room_name')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
