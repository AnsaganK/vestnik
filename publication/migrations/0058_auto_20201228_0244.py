# Generated by Django 3.1.4 on 2020-12-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0057_auto_20201228_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='postCode',
            field=models.CharField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='work',
            field=models.TextField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='workPlace',
            field=models.TextField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
    ]