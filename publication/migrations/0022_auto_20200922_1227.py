# Generated by Django 3.0.5 on 2020-09-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0021_auto_20200919_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='antiplagiat_update_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='redactor_update_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='reviewer_update_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
