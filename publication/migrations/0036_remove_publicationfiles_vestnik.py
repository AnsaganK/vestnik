# Generated by Django 3.0.5 on 2020-11-12 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0035_auto_20201113_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationfiles',
            name='vestnik',
        ),
    ]
