# Generated by Django 5.0 on 2024-11-22 16:31

import hal.labware.models.labware_base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labware", "0002_alter_stackedlabwarezheightchange_z_height_change"),
    ]

    operations = [
        migrations.RenameField(
            model_name="labwarebase",
            old_name="long_side_z_grip_heights",
            new_name="long_side_grip_heights",
        ),
        migrations.RenameField(
            model_name="labwarebase",
            old_name="short_side_z_grip_heights",
            new_name="short_side_grip_heights",
        ),
        migrations.RemoveField(
            model_name="labwarebase",
            name="x_y_z_dimensions",
        ),
        migrations.AddField(
            model_name="labwarebase",
            name="width_depth_height_dimensions",
            field=models.JSONField(
                default=hal.labware.models.labware_base._x_y_z_dimensions_default,
                help_text="Plates are not inheritantly a cube. This property defines how the rectangular shape of the plate changes across heights. Labware is assumed to be landscape such that long side is width (ex. 127mm) and short side is depth (ex. 82mm).",
                verbose_name="X Y Z dimensions",
            ),
        ),
    ]
