from __future__ import annotations

from django.db import models

from .container import Container
from .labware_base import LabwareBase


class PipettableLabware(LabwareBase):
    container = models.ForeignKey(to=Container, on_delete=models.CASCADE)
