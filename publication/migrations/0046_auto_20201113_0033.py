# Generated by Django 3.0.5 on 2020-11-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0045_publicationfiles_vestnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='vestnik',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
