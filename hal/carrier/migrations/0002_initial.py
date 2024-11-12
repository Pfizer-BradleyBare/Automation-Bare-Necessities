# Generated by Django 5.1.2 on 2024-11-12 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("carrier", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("deck", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carrierbase",
            name="deck",
            field=models.ForeignKey(
                help_text="Which deck is this carrier assigned to?",
                on_delete=django.db.models.deletion.CASCADE,
                to="deck.deckbase",
            ),
        ),
        migrations.AddField(
            model_name="carrierbase",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.CreateModel(
            name="HamiltonAutoloadCarrier",
            fields=[
                (
                    "moveablecarrier_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="carrier.moveablecarrier",
                    ),
                ),
                ("carrier_labware_id", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("carrier.moveablecarrier",),
        ),
        migrations.AlterUniqueTogether(
            name="carrierbase",
            unique_together={("deck", "deck_position")},
        ),
    ]
