# Generated by Django 4.1.6 on 2024-07-11 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layout_item', '0009_remove_coverableplate_lid_ptr_coverableplate_lid_id'),
    ]

    operations = [
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
    ]
