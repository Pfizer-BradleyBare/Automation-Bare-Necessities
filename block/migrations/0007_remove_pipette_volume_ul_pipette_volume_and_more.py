# Generated by Django 5.1.2 on 2024-10-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("block", "0006_alter_incubateandshake_shaking_rpm_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pipette",
            name="volume_ul",
        ),
        migrations.AddField(
            model_name="pipette",
            name="volume",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="activatecontainer",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="activatecontainer",
            name="type",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="meta_data_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="meta_data_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="concentrationmax",
            name="constraint_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="concentrationmin",
            name="constraint_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="max_source_volume",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="min_aspirate_mix_cycles",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="min_dispense_mix_cycles",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="solution",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="target_concentration",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="dilute",
            name="target_volume",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="documentnumber",
            name="meta_data_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="incubate",
            name="temperature",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="incubate",
            name="time",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="incubateandshake",
            name="shaking_rpm",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="incubateandshake",
            name="temperature",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="incubateandshake",
            name="time",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="measureconcentration",
            name="extinction_coefficient",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="measureconcentration",
            name="output_worklist_column",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="merge",
            name="container_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="merge",
            name="container_type",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="modality",
            name="meta_data_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="overviewcomment",
            name="comment_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="pipette",
            name="min_aspirate_mix_cycles",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pipette",
            name="min_dispense_mix_cycles",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pipette",
            name="solution",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="meta_data_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="rest",
            name="time",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="runtimecomment",
            name="comment_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="runtimecomment",
            name="wait_for_user_confirmation",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="samplenumbermax",
            name="constraint_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="samplenumbermin",
            name="constraint_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="shake",
            name="shaking_rpm",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="shake",
            name="time",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="silentcomment",
            name="comment_text",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="splitworklist",
            name="container_choice",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="splitworklist",
            name="left_container_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="splitworklist",
            name="left_container_type",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="splitworklist",
            name="right_container_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="splitworklist",
            name="right_container_type",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
