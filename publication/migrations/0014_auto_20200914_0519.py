# Generated by Django 3.0.5 on 2020-09-13 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0013_auto_20200913_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationfiles',
            name='antiplagiat_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='redactor_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='retzenzent_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
