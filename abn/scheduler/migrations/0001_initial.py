# Generated by Django 4.1.6 on 2024-07-26 01:59

from django.db import migrations, models
import scheduler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueuedMethod',
            fields=[
                ('file_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('emails', models.CharField(max_length=100)),
                ('phone_numbers', models.CharField(max_length=100)),
                ('completion_time', models.DateTimeField()),
                ('file', models.FileField(max_length=255, upload_to=scheduler.models.get_upload_path)),
            ],
        ),
    ]
