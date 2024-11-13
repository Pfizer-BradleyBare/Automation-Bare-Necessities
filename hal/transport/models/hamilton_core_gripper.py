from django.db import models

from .transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonCOREGripper(TransportBase):
    gripper_labware_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Hamilton CORE Gripper"
        verbose_name_plural = "Hamilton CORE Grippers"


class HamiltonCOREGripperPickupOptions(TransportPickupOptionsBase):
    transport_device = HamiltonCOREGripper.__name__

    grip_force = models.CharField(
        max_length=25,
        choices=[
            ("Grip Force 0", "Grip Force 0"),
            ("Grip Force 1", "Grip Force 1"),
            ("Grip Force 2", "Grip Force 2"),
            ("Grip Force 3", "Grip Force 3"),
            ("Grip Force 4", "Grip Force 4"),
            ("Grip Force 5", "Grip Force 5"),
            ("Grip Force 6", "Grip Force 6"),
            ("Grip Force 7", "Grip Force 7"),
            ("Grip Force 8", "Grip Force 8"),
            ("Grip Force 9", "Grip Force 9"),
        ],
        default="Grip Force 5",
    )
    grip_speed = models.FloatField(default=277.8)
    z_speed = models.FloatField(default=128.7)
    check_plate_exists = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "grip_force",
            "grip_speed",
            "z_speed",
            "check_plate_exists",
        )

    def __str__(self) -> str:
        return f"grip_force:{self.grip_force}; grip_speed:{self.grip_speed}; z_speed:{self.z_speed}; check_plate_exists:{self.check_plate_exists}"


class HamiltonCOREGripperPlaceOptions(TransportPlaceOptionsBase):
    transport_device = HamiltonCOREGripper.__name__

    x_acceleration_level = models.CharField(
        max_length=25,
        choices=(
            ("Level 1", "Level 1"),
            ("Level 2", "Level 2"),
            ("Level 3", "Level 3"),
            ("Level 4", "Level 4"),
            ("Level 5", "Level 5"),
        ),
        default="Level 4",
    )
    z_speed = models.FloatField(default=128.7)
    plate_press_on_distance = models.FloatField(default=1)
    check_plate_exists = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "x_acceleration_level",
            "z_speed",
            "plate_press_on_distance",
            "check_plate_exists",
        )

    def __str__(self) -> str:
        return f"x_acceleration_level:{self.x_acceleration_level}; z_speed:{self.z_speed}; plate_press_on_distance:{self.plate_press_on_distance}; check_plate_exists:{self.check_plate_exists}"
