# Generated by Django 5.1.2 on 2024-10-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("block", "0008_remove_concentrationmin_blockbase_ptr_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blockbase",
            name="is_valid",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
