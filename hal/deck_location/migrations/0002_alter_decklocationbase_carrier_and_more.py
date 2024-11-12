# Generated by Django 5.1.2 on 2024-11-12 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carrier", "0002_initial"),
        ("deck_location", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="decklocationbase",
            name="carrier",
            field=models.ForeignKey(
                help_text="Which carrier is this deck location assigned to?",
                on_delete=django.db.models.deletion.CASCADE,
                to="carrier.carrierbase",
            ),
        ),
        migrations.AlterField(
            model_name="decklocationbase",
            name="carrier_position",
            field=models.PositiveSmallIntegerField(
                help_text="Typically carriers have multiple plate positions. Position is from front to back."
            ),
        ),
    ]