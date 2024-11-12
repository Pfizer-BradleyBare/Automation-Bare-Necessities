from django.db import models

from .moveable_carrier import MoveableCarrier


class HamiltonAutoloadCarrier(MoveableCarrier):
    carrier_labware_id = models.CharField(
        max_length=50,
        unique=True,
    )
