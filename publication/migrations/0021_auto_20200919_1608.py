# Generated by Django 3.0.5 on 2020-09-19 10:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0020_auto_20200919_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='reviewer_choice',
            field=models.ManyToManyField(blank=True, related_name='rFiles', to=settings.AUTH_USER_MODEL, verbose_name='Рецензенты'),
        ),
    ]