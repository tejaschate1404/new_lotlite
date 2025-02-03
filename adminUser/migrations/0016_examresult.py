# Generated by Django 5.1.4 on 2025-02-02 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0015_mcqquestion_studentanswer_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('exam_date', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.CharField(max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminUser.students')),
            ],
        ),
    ]
