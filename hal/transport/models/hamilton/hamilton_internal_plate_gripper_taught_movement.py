from __future__ import annotations

from django.db import models

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonInternalPlateGripperTaughtMovement(TransportBase):
    @property
    def max_grip_depth(self) -> float:
        return 39


class HamiltonInternalPlateGripperTaughtMovementPickupOptions(
    TransportPickupOptionsBase,
):
    transport_device = HamiltonInternalPlateGripperTaughtMovement.__name__

    taught_path = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}"

    def test_options_equality(
        self: HamiltonInternalPlateGripperTaughtMovementPickupOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonInternalPlateGripperTaughtMovementPickupOptions,
        ):
            return False

        if self.taught_path != value.taught_path:
            return False

        return True


class HamiltonInternalPlateGripperTaughtMovementPlaceOptions(
    TransportPlaceOptionsBase,
):
    transport_device = HamiltonInternalPlateGripperTaughtMovement.__name__

    taught_path = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"taught_path:{self.taught_path}"

    def test_options_equality(
        self: HamiltonInternalPlateGripperTaughtMovementPlaceOptions,
        value: object,
    ) -> bool:
        if not isinstance(
            value,
            HamiltonInternalPlateGripperTaughtMovementPlaceOptions,
        ):
            return False

        if self.taught_path != value.taught_path:
            return False

        return True
