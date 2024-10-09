# Generated by Django 5.1.1 on 2024-10-09 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('method', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateMethodWorkbook',
            fields=[
                ('methodworkbookbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='method.methodworkbookbase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('method.methodworkbookbase',),
        ),
    ]
