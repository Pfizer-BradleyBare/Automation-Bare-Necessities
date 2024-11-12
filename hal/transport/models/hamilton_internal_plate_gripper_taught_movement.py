from django.db import models

from .transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonInternalPlateGripperTaughtMovement(TransportBase): ...


class HamiltonInternalPlateGripperTaughtMovementPickupOptions(
    TransportPickupOptionsBase,
):
    taught_path = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}"


class HamiltonInternalPlateGripperTaughtMovementPlaceOptions(
    TransportPlaceOptionsBase,
):
    taught_path = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}"
