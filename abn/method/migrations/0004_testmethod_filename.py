# Generated by Django 4.1.6 on 2024-07-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0003_remove_testmethod_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmethod',
            name='filename',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]