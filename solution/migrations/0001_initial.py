# Generated by Django 5.1.2 on 2024-11-11 15:32

import django.db.models.deletion
import solution.models.user_defined_component_base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("method", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComponentBase",
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
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="SolutionPropertyPreset",
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
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "liquid_type",
                    models.CharField(
                        choices=[
                            ("Aqueous", "Aqueous"),
                            ("Organic", "Organic"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "viscosity",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "volatility",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "homogeneity",
                    models.CharField(
                        choices=[
                            ("Heterogenous", "Heterogenous"),
                            ("Homogenous", "Homogenous"),
                            ("Suspension", "Suspension"),
                            ("Emulsion", "Emulsion"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PredefinedComponentBase",
            fields=[
                (
                    "componentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.componentbase",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("solution.componentbase",),
        ),
        migrations.CreateModel(
            name="UserDefinedComponentBase",
            fields=[
                (
                    "componentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.componentbase",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "method",
                    models.ForeignKey(
                        on_delete=solution.models.user_defined_component_base.NON_POLYMORPHIC_CASCADE,
                        to="method.methodworkbookbase",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "method")},
            },
            bases=("solution.componentbase",),
        ),
        migrations.CreateModel(
            name="PredefinedComponent",
            fields=[
                (
                    "predefinedcomponentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.predefinedcomponentbase",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("solution.predefinedcomponentbase",),
        ),
        migrations.CreateModel(
            name="UserDefinedComponent",
            fields=[
                (
                    "userdefinedcomponentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.userdefinedcomponentbase",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("solution.userdefinedcomponentbase",),
        ),
        migrations.CreateModel(
            name="SolutionComponent",
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
                ("amount", models.FloatField()),
                (
                    "unit",
                    models.CharField(
                        choices=[("uL", "uL"), ("mg", "mg"), ("units", "units")],
                        max_length=10,
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="solution.componentbase",
                    ),
                ),
            ],
            options={
                "unique_together": {("component", "amount", "unit")},
            },
        ),
        migrations.CreateModel(
            name="PredefinedSolution",
            fields=[
                (
                    "predefinedcomponentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.predefinedcomponentbase",
                    ),
                ),
                (
                    "storage_condition",
                    models.CharField(
                        choices=[("Ambient", "Ambient"), ("Cold", "Cold")], max_length=8
                    ),
                ),
                (
                    "liquid_type",
                    models.CharField(
                        choices=[
                            ("Aqueous", "Aqueous"),
                            ("Organic", "Organic"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "viscosity",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "volatility",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "homogeneity",
                    models.CharField(
                        choices=[
                            ("Heterogenous", "Heterogenous"),
                            ("Homogenous", "Homogenous"),
                            ("Suspension", "Suspension"),
                            ("Emulsion", "Emulsion"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(blank=True, to="solution.solutioncomponent"),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("solution.predefinedcomponentbase",),
        ),
        migrations.CreateModel(
            name="UserDefinedSolution",
            fields=[
                (
                    "userdefinedcomponentbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="solution.userdefinedcomponentbase",
                    ),
                ),
                (
                    "storage_condition",
                    models.CharField(
                        choices=[("Ambient", "Ambient"), ("Cold", "Cold")], max_length=8
                    ),
                ),
                (
                    "liquid_type",
                    models.CharField(
                        choices=[
                            ("Aqueous", "Aqueous"),
                            ("Organic", "Organic"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "viscosity",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "volatility",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "homogeneity",
                    models.CharField(
                        choices=[
                            ("Heterogenous", "Heterogenous"),
                            ("Homogenous", "Homogenous"),
                            ("Suspension", "Suspension"),
                            ("Emulsion", "Emulsion"),
                            ("Auto-determine", "Auto-determine"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(blank=True, to="solution.solutioncomponent"),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("solution.userdefinedcomponentbase",),
        ),
    ]
