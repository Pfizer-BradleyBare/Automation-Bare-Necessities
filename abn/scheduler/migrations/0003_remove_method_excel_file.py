# Generated by Django 4.1.6 on 2024-07-17 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_method_excel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='excel_file',
        ),
    ]
