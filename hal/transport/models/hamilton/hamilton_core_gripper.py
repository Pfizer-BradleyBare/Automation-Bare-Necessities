from __future__ import annotations

from typing import ClassVar

from django.db import models

from hal.layout_item.models import LoadedLayoutItem

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonCOREGripper(TransportBase):
    gripper_labware_id = models.CharField(max_length=100)

    _max_grip_depth:ClassVar[float] = 40

    class Meta:
        verbose_name = "Hamilton CORE Gripper"
        verbose_name_plural = "Hamilton CORE Grippers"

    def transport_time(
        self,
        source: LoadedLayoutItem,
        destination: LoadedLayoutItem,
    ) -> float:
        return 0

    def transport(self, source: LoadedLayoutItem, destination: LoadedLayoutItem):
        self.assert_transport(source,destination)

        grip_height = self.compute_long_side_grip_height(source)


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

    def test_options_equality(
        self: HamiltonCOREGripperPickupOptions,
        value: object,
    ) -> bool:
        if not isinstance(value, HamiltonCOREGripperPickupOptions):
            return False

        return True


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

    def test_options_equality(
        self: HamiltonCOREGripperPlaceOptions,
        value: object,
    ) -> bool:
        if not isinstance(value, HamiltonCOREGripperPlaceOptions):
            return False

        return True
