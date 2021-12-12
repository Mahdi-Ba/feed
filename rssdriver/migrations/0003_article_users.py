# Generated by Django 3.2.10 on 2021-12-10 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rssdriver', '0002_channel_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
