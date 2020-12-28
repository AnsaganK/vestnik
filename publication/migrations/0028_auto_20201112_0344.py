# Generated by Django 3.0.5 on 2020-11-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0027_auto_20201112_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vestnikfiles',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер вестника'),
        ),
        migrations.AlterField(
            model_name='vestnikfiles',
            name='year',
            field=models.CharField(choices=[('2013', 2013), ('2014', 2014), ('2015', 2015), ('2016', 2016), ('2017', 2017), ('2018', 2018), ('2019', 2019), ('2020', 2020)], default=2020, max_length=4, verbose_name='Год вестника'),
        ),
    ]