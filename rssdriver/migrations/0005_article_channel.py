# Generated by Django 3.2.10 on 2021-12-10 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rssdriver', '0004_rename_status_channel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rssdriver.channel'),
        ),
    ]