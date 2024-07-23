# Generated by Django 4.1.6 on 2024-07-23 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labware', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('deck_location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutItemBase',
            fields=[
                ('identifier', models.CharField(default='None', help_text="Unique ID for the item. Leave as 'None' to use an autogenerated identifier.", max_length=50, primary_key=True, serialize=False, unique=True)),
                ('deck_labware_id', models.CharField(max_length=100)),
                ('deck_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_location.decklocationbase')),
                ('labware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labware.labwarebase')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='Lid',
            fields=[
                ('layoutitembase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.layoutitembase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.layoutitembase',),
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('layoutitembase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.layoutitembase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.layoutitembase',),
        ),
        migrations.CreateModel(
            name='TipRack',
            fields=[
                ('layoutitembase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.layoutitembase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.layoutitembase',),
        ),
        migrations.CreateModel(
            name='VacuumManifold',
            fields=[
                ('layoutitembase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.layoutitembase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.layoutitembase',),
        ),
        migrations.CreateModel(
            name='CoverablePlate',
            fields=[
                ('plate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.plate')),
                ('lid_id', models.ForeignKey(db_column='lid_id', on_delete=django.db.models.deletion.CASCADE, to='layout_item.lid')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.plate',),
        ),
        migrations.CreateModel(
            name='FilterPlate',
            fields=[
                ('plate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.plate')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.plate',),
        ),
        migrations.CreateModel(
            name='CoverableFilterPlate',
            fields=[
                ('coverableplate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layout_item.coverableplate')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('layout_item.coverableplate',),
        ),
    ]
