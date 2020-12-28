# Generated by Django 3.0.5 on 2020-11-12 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0036_remove_publicationfiles_vestnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationfiles',
            name='vestnik',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='publications', to='publication.VestnikFiles', verbose_name='Относится к вестнику'),
        ),
    ]
