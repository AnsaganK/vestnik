# Generated by Django 3.0.5 on 2020-11-12 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0041_auto_20201113_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='vestnik',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, related_name='publications', to='publication.VestnikFiles', verbose_name='Относится к вестнику'),
        ),
    ]
