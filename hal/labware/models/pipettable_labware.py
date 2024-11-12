from __future__ import annotations

from django.db import models

from .container import Container
from .labware import Labware


class PipettableLabware(Labware):
    container = models.ForeignKey(to=Container, on_delete=models.CASCADE)
