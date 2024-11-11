# Generated by Django 5.1.2 on 2024-11-11 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("method", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorklistColumn",
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
                ("name", models.CharField(max_length=255)),
                (
                    "method",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="method.methodworkbookbase",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorklistColumnValue",
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
                ("row", models.IntegerField()),
                ("value", models.CharField(max_length=255, null=True)),
                (
                    "worklist_column",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="worklist.worklistcolumn",
                    ),
                ),
            ],
        ),
    ]
