# Generated by Django 4.1.6 on 2024-08-01 17:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('method', '0002_remove_usermethod_filename_alter_usermethod_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutingMethod',
            fields=[
                ('usermethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='method.usermethod')),
                ('state', models.CharField(choices=[('Reading', 'Reading'), ('Running', 'Running'), ('Paused', 'Paused'), ('Waiting on User', 'Waiting on User'), ('Complete', 'Complete'), ('Aborted', 'Aborted')], default='Reading', max_length=15)),
                ('emails', models.CharField(max_length=100)),
                ('phone_numbers', models.CharField(blank=True, max_length=100)),
                ('desired_completion_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('method.usermethod',),
        ),
        migrations.CreateModel(
            name='TestingMethod',
            fields=[
                ('usermethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='method.usermethod')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('method.usermethod',),
        ),
        migrations.AlterModelOptions(
            name='usermethod',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='usermethod',
            name='activity',
        ),
        migrations.AddField(
            model_name='usermethod',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermethod',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
