from django.db import models
from django.forms import ValidationError
from polymorphic.models import PolymorphicModel


class LabwareBase(PolymorphicModel):
    class Meta:
        ordering = ["identifier"]

    identifier = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
    )

    x_length = models.FloatField()
    y_length = models.FloatField()

    transport_open_offset = models.FloatField()
    transport_close_offset = models.FloatField()
    transport_top_offset = models.FloatField()
    transport_bottom_offset = models.FloatField()

    labware_definition_type = models.CharField(
        max_length=12,
        choices=(("Numeric", "Numeric"), ("Alphanumeric", "Alphanumeric")),
    )

    def __str__(self) -> str:
        return self.identifier


class NonPipettableLabware(LabwareBase): ...


class PipettableLabware(LabwareBase):
    positions_per_well = models.SmallIntegerField()
    well_max_volume = models.FloatField()
    well_dead_volume = models.FloatField()
    calibration_points = models.JSONField(
        help_text="Should be a list of dictionary values containing 'Volume' and 'Height' where 'Volume' is in uL and 'Height' is in mm. Ex. [{\"Volume\":0,\"Height\":0},{\"Volume\":100,\"Height\":10}]",
    )

    def clean(self) -> None:
        error_msg = "Calibration points input must be a list of Height, Volume dict. See help text for example."

        if not isinstance(self.calibration_points, list):
            raise ValidationError(error_msg)

        for item in self.calibration_points:
            if not isinstance(item, dict):
                raise ValidationError(error_msg)
            if "Height" not in item:
                raise ValidationError(error_msg)
            if "Volume" not in item:
                raise ValidationError(error_msg)

        return super().clean()
