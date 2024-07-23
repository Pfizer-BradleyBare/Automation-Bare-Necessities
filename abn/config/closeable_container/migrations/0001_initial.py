# Generated by Django 4.1.6 on 2024-07-23 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('backend', '0001_initial'),
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
