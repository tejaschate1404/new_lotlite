# Generated by Django 5.1.4 on 2025-02-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0013_students_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='student',
        ),
        migrations.AddField(
            model_name='students',
            name='branch',
            field=models.CharField(default='CSE', max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='roll_no',
            field=models.CharField(default='0000', max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='year',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
