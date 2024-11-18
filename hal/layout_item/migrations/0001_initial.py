# Generated by Django 5.0 on 2024-11-18 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("backend", "0001_initial"),
        ("carrier_location", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("labware", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LayoutItemBase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identifier", models.CharField(editable=False, max_length=255)),
                (
                    "carrier_location",
                    models.ForeignKey(
                        help_text="Which deck location is this layout item located?",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrier_location.carrierlocationbase",
                    ),
                ),
                (
                    "labware",
                    models.ForeignKey(
                        help_text="What is the labware of this layout item?",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="labware.labwarebase",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "ordering": ["identifier"],
                "unique_together": {("carrier_location", "labware")},
            },
        ),
        migrations.CreateModel(
            name="HamiltonLayoutItem",
            fields=[
                (
                    "layoutitembase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="layout_item.layoutitembase",
                    ),
                ),
                ("venus_labware_id", models.CharField(max_length=255, unique=True)),
                (
                    "backend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.hamiltonbackendbase",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("layout_item.layoutitembase",),
        ),
        migrations.CreateModel(
            name="LayoutItemStack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stack_position", models.PositiveIntegerField()),
                (
                    "carrier_location",
                    models.ForeignKey(
                        help_text="Which deck location is this layout item located?",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrier_location.carrierlocationbase",
                    ),
                ),
                (
                    "layout_item",
                    models.ForeignKey(
                        help_text="What is the labware of this layout item?",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="labware.labwarebase",
                    ),
                ),
            ],
            options={
                "ordering": ["stack_position"],
                "unique_together": {
                    ("carrier_location", "layout_item", "stack_position")
                },
            },
        ),
    ]
