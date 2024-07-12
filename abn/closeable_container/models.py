from backend.models import BackendBase
from deck_location.models import DeckLocationBase
from django.db import models
from labware.models import LabwareBase
from polymorphic.models import PolymorphicModel


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
