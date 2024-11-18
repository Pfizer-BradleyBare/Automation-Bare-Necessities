from __future__ import annotations

from django.db import models

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonInternalPlateGripperComplexMovement(TransportBase): ...


class HamiltonInternalPlateGripperComplexMovementPickupOptions(
    TransportPickupOptionsBase,
):
    transport_device = HamiltonInternalPlateGripperComplexMovement.__name__

    grip_mode = models.CharField(
        max_length=20,
        choices=(
            ("Grip on short side", "Grip on short side"),
            ("Grip on long side", "Grip on long side"),
        ),
    )
    retract_distance = models.FloatField()
    liftup_height = models.FloatField()
    labware_orientation = models.CharField(
        max_length=25,
        choices=[
            ("Positive Y Direction", "Positive Y Direction"),
            ("Negative X Direction", "Negative X Direction"),
            ("Negative Y Direction", "Negative Y Direction"),
            ("Positive X Direction", "Positive X Direction"),
        ],
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
    inverse_grip = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "grip_mode",
            "retract_distance",
            "liftup_height",
            "labware_orientation",
            "grip_force",
            "tolerance",
            "inverse_grip",
        )

    def __str__(self) -> str:
        return f"grip_mode:{self.grip_mode}; retract_distance:{self.retract_distance}; liftup_height:{self.liftup_height}; labware_orientation:{self.labware_orientation}; grip_force:{self.grip_force}; tolerance:{self.tolerance}; inverse_grip:{self.inverse_grip}"

    def test_options_equality(
        self: HamiltonInternalPlateGripperComplexMovementPickupOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonInternalPlateGripperComplexMovementPickupOptions,
        ):
            return False

        if self.grip_mode != value.grip_mode:
            return False

        if self.labware_orientation != value.labware_orientation:
            return False

        if self.inverse_grip != value.inverse_grip:
            return False

        return True


class HamiltonInternalPlateGripperComplexMovementPlaceOptions(
    TransportPlaceOptionsBase,
):
    transport_device = HamiltonInternalPlateGripperComplexMovement.__name__

    retract_distance = models.FloatField()
    liftup_height = models.FloatField
    labware_orientation = models.CharField(
        max_length=25,
        choices=[
            ("Positive Y Direction", "Positive Y Direction"),
            ("Negative X Direction", "Negative X Direction"),
            ("Negative Y Direction", "Negative Y Direction"),
            ("Positive X Direction", "Positive X Direction"),
        ],
    )

    def __str__(self) -> str:
        return f"retract_distance:{self.retract_distance}; liftup_height:{self.liftup_height}; labware_orientation:{self.labware_orientation}"

    def test_options_equality(
        self: HamiltonInternalPlateGripperComplexMovementPlaceOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonInternalPlateGripperComplexMovementPlaceOptions,
        ):
            return False

        if self.labware_orientation != value.labware_orientation:
            return False

        return True
