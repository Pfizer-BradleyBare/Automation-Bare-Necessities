# Generated by Django 5.0 on 2024-11-21 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("layout_item", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoadedLayoutItem",
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
                (
                    "bottom",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="layout_item.loadedlayoutitem",
                    ),
                ),
                (
                    "layout_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="layout_item.layoutitembase",
                    ),
                ),
                (
                    "top",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="layout_item.loadedlayoutitem",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="LayoutItemStack",
        ),
    ]