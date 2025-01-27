# Generated by Django 5.1.4 on 2025-01-24 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUser', '0009_categoryservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('primary_desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='adminUser.categoryservices')),
            ],
        ),
    ]
