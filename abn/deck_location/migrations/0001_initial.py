# Generated by Django 4.1.6 on 2024-07-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeckLocationBase',
            fields=[
                ('identifier', models.CharField(default='None', help_text="Unique ID for the item. Leave as 'None' to use an autogenerated identifier.", max_length=50, primary_key=True, serialize=False, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='TransportConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NonTransportableDeckLocation',
            fields=[
                ('decklocationbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='deck_location.decklocationbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('deck_location.decklocationbase',),
        ),
        migrations.CreateModel(
            name='TransportableDeckLocation',
            fields=[
                ('decklocationbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='deck_location.decklocationbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('deck_location.decklocationbase',),
        ),
    ]
