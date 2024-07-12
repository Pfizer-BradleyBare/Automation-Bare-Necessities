# Generated by Django 4.1.6 on 2024-07-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deck_location', '0001_initial'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='TransportConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
