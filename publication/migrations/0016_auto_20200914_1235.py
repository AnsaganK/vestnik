# Generated by Django 3.0.5 on 2020-09-14 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0015_auto_20200914_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='antiplagiat_update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 12, 35, 40, 352282)),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='redactor_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='retzenzent_update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 12, 35, 40, 352282)),
        ),
    ]