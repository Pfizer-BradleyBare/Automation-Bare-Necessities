# Generated by Django 5.1.1 on 2024-09-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('closeable_container', '0002_initial'),
        ('labware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='closeablecontainerbase',
            name='supported_labwares',
            field=models.ManyToManyField(to='labware.labwarebase'),
        ),
    ]
