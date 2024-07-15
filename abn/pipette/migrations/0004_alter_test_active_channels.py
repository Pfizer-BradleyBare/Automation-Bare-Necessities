# Generated by Django 4.1.6 on 2024-07-15 20:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pipette', '0003_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='active_channels',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], max_length=100),
        ),
    ]
