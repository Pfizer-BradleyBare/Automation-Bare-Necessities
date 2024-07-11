# Generated by Django 4.1.6 on 2024-07-11 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck_location', '0002_delete_carrierconfig'),
        ('labware', '0002_alter_pipettablelabware_calibration_points'),
        ('contenttypes', '0002_remove_content_type_name'),
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
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
    ]
