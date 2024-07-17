# Generated by Django 4.1.6 on 2024-07-17 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentrifugeBase',
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
            name='HamiltonHiG4',
            fields=[
                ('centrifugebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='centrifuge.centrifugebase')),
                ('adapter_id', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Hamilton HiG4',
                'verbose_name_plural': 'Hamilton HiG4s',
            },
            bases=('centrifuge.centrifugebase',),
        ),
    ]
