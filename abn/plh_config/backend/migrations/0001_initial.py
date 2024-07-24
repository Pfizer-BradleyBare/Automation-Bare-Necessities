# Generated by Django 4.1.6 on 2024-07-24 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackendBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='HamiltonBackendBase',
            fields=[
                ('backendbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.backendbase')),
                ('deck_layout', models.FilePathField(help_text='Custom made layouts can be placed in any sub folder in the parent folder: C:\\Program Files (x86)\\HAMILTON\\Methods\\plh', match='^(?!active_layout\\.lay|blank_layout\\.lay).*\\.lay$', path='C:\\Program Files (x86)\\HAMILTON\\Methods\\plh', recursive=True)),
                ('simulation_on', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('backend.backendbase',),
        ),
        migrations.CreateModel(
            name='Stunner',
            fields=[
                ('backendbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.backendbase')),
                ('ip_address', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('backend.backendbase',),
        ),
        migrations.CreateModel(
            name='HamiltonMicrolabStar',
            fields=[
                ('hamiltonbackendbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.hamiltonbackendbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('backend.hamiltonbackendbase',),
        ),
        migrations.CreateModel(
            name='HamiltonTrackGripperEntryExitVantage',
            fields=[
                ('hamiltonbackendbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.hamiltonbackendbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('backend.hamiltonbackendbase',),
        ),
    ]
