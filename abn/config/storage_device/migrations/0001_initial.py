# Generated by Django 4.1.6 on 2024-07-23 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('layout_item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageDeviceBase',
            fields=[
                ('identifier', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('layout_items', models.ManyToManyField(to='layout_item.layoutitembase')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.CreateModel(
            name='RandomAccessDeckStorage',
            fields=[
                ('storagedevicebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage_device.storagedevicebase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('storage_device.storagedevicebase',),
        ),
    ]
