# Generated by Django 3.0.5 on 2020-11-12 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0030_publicationfiles_vestnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationfiles',
            name='vestnik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publication.VestnikFiles', verbose_name='Относится к вестнику'),
        ),
    ]