from __future__ import annotations

from django.db import models

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonVantageTrackGripperTaughtMovement(TransportBase): ...


class HamiltonVantageTrackGripperTaughtMovementPickupOptions(
    TransportPickupOptionsBase,
):
    transport_device = HamiltonVantageTrackGripperTaughtMovement.__name__

    taught_path = models.CharField(max_length=255, unique=True)
    grip_force_percent = models.FloatField()
    movement_speed_percent = models.FloatField()
    coordinated_movement = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "taught_path",
            "grip_force_percent",
            "movement_speed_percent",
            "coordinated_movement",
        )

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}; grip_force_percent:{self.grip_force_percent}; movement_speed_percent:{self.movement_speed_percent}; coordinated_movement:{self.coordinated_movement}"

    def test_options_equality(
        self: HamiltonVantageTrackGripperTaughtMovementPickupOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonVantageTrackGripperTaughtMovementPickupOptions,
        ):
            return False

        if self.taught_path != value.taught_path:
            return False

        return True


class HamiltonVantageTrackGripperTaughtMovementPlaceOptions(TransportPlaceOptionsBase):
    transport_device = HamiltonVantageTrackGripperTaughtMovement.__name__

    taught_path = models.CharField(max_length=255, unique=True)
    movement_speed_percent = models.FloatField()
    coordinated_movement = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "taught_path",
            "movement_speed_percent",
            "coordinated_movement",
        )

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}; movement_speed_percent:{self.movement_speed_percent}; coordinated_movement:{self.coordinated_movement}"

    def test_options_equality(
        self: HamiltonVantageTrackGripperTaughtMovementPlaceOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonVantageTrackGripperTaughtMovementPlaceOptions,
        ):
            return False

        if self.taught_path != value.taught_path:
            return False

        return True
