from django.db import models
from polymorphic.models import PolymorphicModel

from abn_config.backend.models import BackendBase
from abn_config.deck_location.models import DeckLocationBase
from abn_config.labware.models import LabwareBase


class CloseableContainerBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    enabled = models.BooleanField(default=True)

    backend = models.ForeignKey(to=BackendBase, on_delete=models.CASCADE)

    supported_deck_locations = models.ManyToManyField(to=DeckLocationBase)

    supported_labwares = models.ManyToManyField(to=LabwareBase)


class HamiltonFliptubeLandscape(CloseableContainerBase):
    tool_labware_id = models.CharField(max_length=100)
