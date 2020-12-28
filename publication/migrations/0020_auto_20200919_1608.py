# Generated by Django 3.0.5 on 2020-09-19 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0019_auto_20200916_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_choice',
            field=models.ManyToManyField(blank=True, null=True, related_name='rFiles', to=settings.AUTH_USER_MODEL, verbose_name='Рецензенты'),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]