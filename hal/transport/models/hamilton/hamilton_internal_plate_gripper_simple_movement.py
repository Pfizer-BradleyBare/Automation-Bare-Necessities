from django.db import models

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonInternalPlateGripperSimpleMovement(TransportBase): ...


class HamiltonInternalPlateGripperSimpleMovementPickupOptions(
    TransportPickupOptionsBase,
):
    transport_device = HamiltonInternalPlateGripperSimpleMovement.__name__

    grip_mode = models.CharField(
        max_length=20,
        choices=(
            ("Grip on short side", "Grip on short side"),
            ("Grip on long side", "Grip on long side"),
        ),
    )
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
    tolerance = models.FloatField(default=2)
    inverse_grip = models.BooleanField()

    class Meta:
        unique_together = (
            "grip_mode",
            "grip_force",
            "tolerance",
            "inverse_grip",
        )

    def __str__(self) -> str:
        return f"grip_mode:{self.grip_mode}; grip_force:{self.grip_force}; tolerance:{self.tolerance}; inverse_grip:{self.inverse_grip}"


class HamiltonInternalPlateGripperSimpleMovementPlaceOptions(TransportPlaceOptionsBase):
    transport_device = HamiltonInternalPlateGripperSimpleMovement.__name__

    def __str__(self) -> str:
        return "Default place options"
