# Generated by Django 3.1.4 on 2020-12-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0058_auto_20201228_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='basic',
            field=models.BooleanField(default=False),
        ),
    ]