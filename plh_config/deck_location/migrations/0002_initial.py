# Generated by Django 5.1.1 on 2024-10-02 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck_location', '0001_initial'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportconfig',
            name='get_options',
            field=models.ManyToManyField(to='transport.transportgetoptions'),
        ),
        migrations.AddField(
            model_name='transportconfig',
            name='place_options',
            field=models.ManyToManyField(to='transport.transportplaceoptions'),
        ),
        migrations.AddField(
            model_name='transportconfig',
            name='transport_device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.transportbase'),
        ),
        migrations.AddField(
            model_name='transportabledecklocation',
            name='transport_configs',
            field=models.ManyToManyField(to='deck_location.transportconfig'),
        ),
    ]
