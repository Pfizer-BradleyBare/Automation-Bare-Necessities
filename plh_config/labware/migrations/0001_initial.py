# Generated by Django 5.1.1 on 2024-09-25 21:32

import django.db.models.deletion
import plh_config.labware.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabwareBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('x_length', models.FloatField()),
                ('y_length', models.FloatField()),
                ('z_length', models.FloatField()),
                ('transport_open_offset', models.FloatField()),
                ('transport_close_offset', models.FloatField()),
                ('transport_top_offset', models.FloatField()),
                ('transport_bottom_offset', models.FloatField()),
                ('labware_definition_type', models.CharField(choices=[('Numeric', 'Numeric'), ('Alphanumeric', 'Alphanumeric')], max_length=12)),
                ('labware_definition_direction', models.CharField(choices=[('Rowwise', 'Rowwise'), ('Columnwise', 'Columnwise')], max_length=12)),
                ('labware_defintion_columns', models.SmallIntegerField()),
                ('labware_defintion_rows', models.SmallIntegerField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='NonPipettableLabware',
            fields=[
                ('labwarebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='labware.labwarebase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('labware.labwarebase',),
        ),
        migrations.CreateModel(
            name='PipettableLabware',
            fields=[
                ('labwarebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='labware.labwarebase')),
                ('positions_per_well', models.SmallIntegerField()),
                ('well_max_volume', models.FloatField()),
                ('well_dead_volume', models.FloatField()),
                ('calibration_points', models.JSONField(default=plh_config.labware.models.json_default, help_text='Should be a list of dictionary values containing \'Volume\' and \'Height\' where \'Volume\' is in uL and \'Height\' is in mm. Ex. [{"Volume":0,"Height":0},{"Volume":100,"Height":10}]')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('labware.labwarebase',),
        ),
    ]
