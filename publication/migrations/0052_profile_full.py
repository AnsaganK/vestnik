# Generated by Django 3.0.5 on 2020-11-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0051_auto_20201115_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
