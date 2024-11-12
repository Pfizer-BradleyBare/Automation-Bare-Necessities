from django.db import models

from .transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonVantageTrackGripperTaughtMovement(TransportBase): ...


class HamiltonVantageTrackGripperTaughtMovementPickupOptions(
    TransportPickupOptionsBase,
):
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


class HamiltonVantageTrackGripperTaughtMovementPlaceOptions(TransportPlaceOptionsBase):
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
