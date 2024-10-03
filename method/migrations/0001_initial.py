# Generated by Django 5.1.1 on 2024-10-03 21:48

import django.db.models.deletion
import method.models.user_method_workbook_base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMethodWorkbookBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(max_length=255, storage=method.models.user_method_workbook_base.CustomStorage, upload_to=method.models.user_method_workbook_base.upload_to)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ExecutingMethodWorkbook',
            fields=[
                ('usermethodworkbookbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='method.usermethodworkbookbase')),
                ('state', models.CharField(choices=[('Reading', 'Reading'), ('Running', 'Running'), ('Paused', 'Paused'), ('Waiting on User', 'Waiting on User'), ('Complete', 'Complete'), ('Aborted', 'Aborted'), ('Cleanup', 'Cleanup')], default='Reading', max_length=15)),
                ('emails', models.CharField(max_length=100)),
                ('phone_numbers', models.CharField(blank=True, max_length=100)),
                ('desired_completion_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('method.usermethodworkbookbase',),
        ),
        migrations.CreateModel(
            name='TestingMethodWorkbook',
            fields=[
                ('usermethodworkbookbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='method.usermethodworkbookbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('method.usermethodworkbookbase',),
        ),
    ]
