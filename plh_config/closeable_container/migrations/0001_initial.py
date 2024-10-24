# Generated by Django 5.1.1 on 2024-10-09 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloseableContainerBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.backendbase')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='HamiltonFliptubeLandscape',
            fields=[
                ('closeablecontainerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='closeable_container.closeablecontainerbase')),
                ('tool_labware_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('closeable_container.closeablecontainerbase',),
        ),
    ]
