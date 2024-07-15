# Generated by Django 4.1.6 on 2024-07-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrierBase',
            fields=[
                ('identifier', models.CharField(default='None', help_text="Unique ID for the item. Leave as 'None' to use an autogenerated identifier.", max_length=50, primary_key=True, serialize=False, unique=True)),
                ('track_start', models.PositiveSmallIntegerField()),
                ('track_end', models.PositiveSmallIntegerField()),
                ('num_labware_positions', models.PositiveSmallIntegerField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='MoveableCarrier',
            fields=[
                ('carrierbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carrier.carrierbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('carrier.carrierbase',),
        ),
        migrations.CreateModel(
            name='NonMoveableCarrier',
            fields=[
                ('carrierbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carrier.carrierbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('carrier.carrierbase',),
        ),
        migrations.CreateModel(
            name='HamiltonAutoloadCarrier',
            fields=[
                ('moveablecarrier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='carrier.moveablecarrier')),
                ('carrier_labware_id', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('carrier.moveablecarrier',),
        ),
    ]
