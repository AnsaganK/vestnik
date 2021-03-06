# Generated by Django 3.0.5 on 2020-09-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0018_auto_20200914_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicationfiles',
            old_name='retzenzent',
            new_name='reviewer',
        ),
        migrations.RenameField(
            model_name='publicationfiles',
            old_name='retzenzent_file',
            new_name='reviewer_file',
        ),
        migrations.RenameField(
            model_name='publicationfiles',
            old_name='retzenzent_update_time',
            new_name='reviewer_update_time',
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='redactor_error',
            field=models.BooleanField(default=False, verbose_name='Редактор(Ошибка)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='redactor_error_text',
            field=models.TextField(blank=True, null=True, verbose_name='Редактор(Текст ошибки)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='redactor_return',
            field=models.BooleanField(default=False, verbose_name='Редактор(возврат)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='redactor_return_text',
            field=models.TextField(blank=True, null=True, verbose_name='Редактор(Текст возврата)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_error',
            field=models.BooleanField(default=False, verbose_name='Рецензент(Ошибка)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_error_text',
            field=models.TextField(blank=True, null=True, verbose_name='Рецензент(Текст ошибки)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_return',
            field=models.BooleanField(default=False, verbose_name='Рецензент(возврат)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_return_text',
            field=models.TextField(blank=True, null=True, verbose_name='Рецензент(Текст возврата)'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='reviewer_text',
            field=models.TextField(blank=True, null=True, verbose_name='Рецензент(Текст)'),
        ),
    ]
