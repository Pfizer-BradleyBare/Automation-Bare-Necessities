# Generated by Django 4.1.6 on 2024-07-26 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeatCoolShakeBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.backendbase')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='HamiltonHeaterCooler',
            fields=[
                ('heatcoolshakebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heat_cool_shake.heatcoolshakebase')),
                ('com_port', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('heat_cool_shake.heatcoolshakebase',),
        ),
        migrations.CreateModel(
            name='HamiltonHeaterShaker',
            fields=[
                ('heatcoolshakebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heat_cool_shake.heatcoolshakebase')),
                ('com_port', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('heat_cool_shake.heatcoolshakebase',),
        ),
    ]
