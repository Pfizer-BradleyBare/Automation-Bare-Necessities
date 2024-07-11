from deck_location.models import DeckLocationBase
from django.db import models
from django.forms import ValidationError
from labware.models import LabwareBase, NonPipettableLabware, PipettableLabware
from polymorphic.models import PolymorphicModel


# Create your models here.
class LayoutItemBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
        default="None",
        help_text="Unique ID for the item. Leave as 'None' to use an autogenerated identifier.",
    )
    deck_labware_id = models.CharField(max_length=100)

    deck_location = models.ForeignKey(
        to=DeckLocationBase,
        on_delete=models.CASCADE,
    )
    labware = models.ForeignKey(
        to=LabwareBase,
        on_delete=models.CASCADE,
    )

    def clean(self) -> None:
        if self.identifier.lower() == "none":
            self.identifier = (
                f"{self.deck_location.identifier}_{self.labware.identifier}"
            )

        return super().clean()

    def __str__(self) -> str:
        return self.identifier


class Lid(LayoutItemBase):
    def clean(self) -> None:
        if not isinstance(self.labware, NonPipettableLabware):
            raise ValidationError("Labware choice must be a pipettable labware.")
        return super().clean()


class TipRack(LayoutItemBase):
    def clean(self) -> None:
        if not isinstance(self.labware, NonPipettableLabware):
            raise ValidationError("Labware choice must be a pipettable labware.")
        return super().clean()


class VacuumManifold(LayoutItemBase):
    def clean(self) -> None:
        if not isinstance(self.labware, NonPipettableLabware):
            raise ValidationError("Labware choice must be a pipettable labware.")
        return super().clean()


class Plate(LayoutItemBase):
    def clean(self) -> None:
        if not isinstance(self.labware, PipettableLabware):
            raise ValidationError("Labware choice must be a pipettable labware.")
        return super().clean()


class FilterPlate(Plate): ...


class CoverablePlate(Plate):
    lid = models.ForeignKey(
        to=Lid,
        on_delete=models.CASCADE,
        name="lid_id",
        db_column="lid_id",
    )


class CoverableFilterPlate(CoverablePlate): ...
