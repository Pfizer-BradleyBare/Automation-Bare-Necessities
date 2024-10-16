# Generated by Django 5.1.1 on 2024-10-09 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipette', '0001_initial'),
        ('tip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipettetip',
            name='tip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tip.tipbase'),
        ),
        migrations.AddField(
            model_name='pipettebase',
            name='supported_tips',
            field=models.ManyToManyField(to='pipette.pipettetip'),
        ),
        migrations.CreateModel(
            name='HamiltonPortraitCORE8SimpleContentDispense',
            fields=[
                ('hamiltonportraitcore8_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipette.hamiltonportraitcore8')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('pipette.hamiltonportraitcore8',),
        ),
    ]
