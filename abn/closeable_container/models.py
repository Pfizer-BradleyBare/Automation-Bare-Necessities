from backend.models import BackendBase, HamiltonBackendBase
from deck_location.models import DeckLocationBase
from django.db import models
from django.forms import ValidationError
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

    supported_labware = models.ManyToManyField(to=LabwareBase)


class HamiltonFliptubeLandscape(CloseableContainerBase):
    tool_labware_id = models.CharField(max_length=100)

    def clean(self) -> None:
        if not isinstance(self.backend, HamiltonBackendBase):
            raise ValidationError("Backend choice must be a Hamilton backend.")
        return super().clean()
