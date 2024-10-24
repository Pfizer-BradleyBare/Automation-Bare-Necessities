# Generated by Django 5.1.1 on 2024-10-09 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('left_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase')),
                ('left_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='block.blockbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ActivateContainer',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('meta_data_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('meta_data_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='ConcentrationMax',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('constraint_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='ConcentrationMin',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('constraint_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Dilute',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('solution', models.CharField(max_length=255)),
                ('target_concentration', models.CharField(max_length=255)),
                ('target_volume', models.CharField(max_length=255)),
                ('min_aspirate_mix_cycles', models.CharField(blank=True, max_length=255)),
                ('min_dispense_mix_cycles', models.CharField(blank=True, max_length=255)),
                ('max_source_volume', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Incubate',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('time', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='IncubateAndShake',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('time', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
                ('shaking_rpm', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='INXNumber',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('meta_data_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='MeasureConcentration',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('output_worklist_column', models.CharField(max_length=255)),
                ('extinction_coefficient', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Merge',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('container_name', models.CharField(max_length=255)),
                ('container_type', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='MethodStart',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('meta_data_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='OverviewComment',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('comment_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Pipette',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('solution', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
                ('min_aspirate_mix_cycles', models.CharField(blank=True, max_length=255)),
                ('min_dispense_mix_cycles', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('time', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='RuntimeComment',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('comment_text', models.TextField()),
                ('wait_for_user_confirmation', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='SampleNumberMax',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('constraint_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='SampleNumberMin',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('constraint_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('meta_data_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='Shake',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('time', models.CharField(max_length=255)),
                ('shaking_rpm', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='SilentComment',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('comment_text', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
        migrations.CreateModel(
            name='SplitWorklist',
            fields=[
                ('blockbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='block.blockbase')),
                ('left_container_name', models.CharField(max_length=255)),
                ('left_container_type', models.CharField(blank=True, max_length=255)),
                ('right_container_name', models.CharField(max_length=255)),
                ('right_container_type', models.CharField(blank=True, max_length=255)),
                ('container_choice', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('block.blockbase',),
        ),
    ]
