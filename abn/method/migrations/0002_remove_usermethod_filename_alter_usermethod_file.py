# Generated by Django 4.1.6 on 2024-08-01 16:20

from django.db import migrations, models
import method.models


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermethod',
            name='filename',
        ),
        migrations.AlterField(
            model_name='usermethod',
            name='file',
            field=models.FileField(max_length=255, storage=method.models.CustomStorage, upload_to=method.models.upload_to),
        ),
    ]
