# Generated by Django 3.1.4 on 2020-12-27 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0053_auto_20201116_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pages',
            name='submenu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publication.pages'),
        ),
    ]
