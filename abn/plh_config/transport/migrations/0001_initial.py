# Generated by Django 4.1.6 on 2024-08-01 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('labware', '0001_initial'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.backendbase')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('supported_labwares', models.ManyToManyField(to='labware.labwarebase')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='TransportGetOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TransportPlaceOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='HamiltonCOREGripper',
            fields=[
                ('transportbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportbase')),
                ('gripper_labware_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Hamilton CORE Gripper',
                'verbose_name_plural': 'Hamilton CORE Grippers',
            },
            bases=('transport.transportbase',),
        ),
        migrations.CreateModel(
            name='HamiltonCOREGripperGetOptions',
            fields=[
                ('transportgetoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportgetoptions')),
                ('check_plate_exists', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportgetoptions',),
        ),
        migrations.CreateModel(
            name='HamiltonCOREGripperPlaceOptions',
            fields=[
                ('transportplaceoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportplaceoptions')),
                ('check_plate_exists', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportplaceoptions',),
        ),
        migrations.CreateModel(
            name='HamiltonInternalPlateGripper',
            fields=[
                ('transportbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportbase',),
        ),
        migrations.CreateModel(
            name='HamiltonInternalPlateGripperGetOptions',
            fields=[
                ('transportgetoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportgetoptions')),
                ('grip_mode', models.CharField(choices=[('GripOnShortSide', 'Grip On Short Side'), ('GripOnLongSide', 'Grip On Long Side')], max_length=20)),
                ('movement', models.CharField(choices=[('Carrier', 'Carrier'), ('Complex', 'Complex')], max_length=20)),
                ('retract_distance', models.FloatField()),
                ('liftup_height', models.FloatField()),
                ('labware_orientation', models.CharField(choices=[('NegativeYAxis', 'Negative Y Axis'), ('PositiveXAxis', 'Positive X Axis'), ('PositiveYAxis', 'Positive Y Axis'), ('NegativeXAxis', 'Negative X Axis')], max_length=20)),
                ('inverse_grip', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportgetoptions',),
        ),
        migrations.CreateModel(
            name='HamiltonInternalPlateGripperPlaceOptions',
            fields=[
                ('transportplaceoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportplaceoptions')),
                ('movement', models.CharField(choices=[('Carrier', 'Carrier'), ('Complex', 'Complex')], max_length=20)),
                ('retract_distance', models.FloatField()),
                ('liftup_height', models.FloatField()),
                ('labware_orientation', models.CharField(choices=[('NegativeYAxis', 'Negative Y Axis'), ('PositiveXAxis', 'Positive X Axis'), ('PositiveYAxis', 'Positive Y Axis'), ('NegativeXAxis', 'Negative X Axis')], max_length=20)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportplaceoptions',),
        ),
        migrations.CreateModel(
            name='VantageTrackGripper',
            fields=[
                ('transportbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportbase',),
        ),
        migrations.CreateModel(
            name='VantageTrackGripperGetOptions',
            fields=[
                ('transportgetoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportgetoptions')),
                ('park_labware_id', models.CharField(blank=True, max_length=100)),
                ('taught_path_name', models.CharField(max_length=100)),
                ('path_execution_time', models.FloatField()),
                ('labware_orientation', models.CharField(choices=[('NegativeYAxis', 'Negative Y Axis'), ('PositiveXAxis', 'Positive X Axis'), ('PositiveYAxis', 'Positive Y Axis'), ('NegativeXAxis', 'Negative X Axis')], max_length=20)),
                ('coordinated_movement', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportgetoptions',),
        ),
        migrations.CreateModel(
            name='VantageTrackGripperPlaceOptions',
            fields=[
                ('transportplaceoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transport.transportplaceoptions')),
                ('park_labware_id', models.CharField(blank=True, max_length=100)),
                ('taught_path_name', models.CharField(max_length=100)),
                ('path_execution_time', models.FloatField()),
                ('coordinated_movement', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('transport.transportplaceoptions',),
        ),
    ]
