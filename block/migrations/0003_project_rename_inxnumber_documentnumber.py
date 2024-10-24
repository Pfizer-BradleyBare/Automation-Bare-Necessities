# Generated by Django 5.1.1 on 2024-10-09 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
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
        migrations.RenameModel(
            old_name='INXNumber',
            new_name='DocumentNumber',
        ),
    ]
