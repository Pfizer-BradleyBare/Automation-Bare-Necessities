# Generated by Django 5.0 on 2024-11-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transport", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transportbase",
            name="last_transport_flag",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]