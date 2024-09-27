# Generated by Django 5.1.1 on 2024-09-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('closeable_container', '0001_initial'),
        ('deck_location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='closeablecontainerbase',
            name='supported_deck_locations',
            field=models.ManyToManyField(to='deck_location.decklocationbase'),
        ),
    ]
