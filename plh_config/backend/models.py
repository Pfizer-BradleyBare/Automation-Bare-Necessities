from django.db import models
from polymorphic.models import PolymorphicModel


class BackendBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return self.identifier


class HamiltonBackendBase(BackendBase):
    deck_layout = models.FilePathField(
        path="C:\\Program Files (x86)\\HAMILTON\\Methods\\plh",
        match=r"^(?!active_layout\.lay|blank_layout\.lay).*\.lay$",
        recursive=True,
        help_text="Custom made layouts can be placed in any sub folder in the parent folder: C:\\Program Files (x86)\\HAMILTON\\Methods\\plh",
    )
    simulation_on = models.BooleanField()


class VantageTrackGripperEntryExit(HamiltonBackendBase): ...


class MicrolabStar(HamiltonBackendBase): ...


class Stunner(BackendBase):
    ip_address = models.CharField(max_length=50)
    port = models.SmallIntegerField
