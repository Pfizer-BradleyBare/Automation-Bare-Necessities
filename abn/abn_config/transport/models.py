from django.db import models
from polymorphic.models import PolymorphicModel

from abn_config.backend.models import BackendBase
from abn_config.labware.models import LabwareBase


class TransportBase(PolymorphicModel):
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

    supported_labwares = models.ManyToManyField(to=LabwareBase)

    def __str__(self) -> str:
        return self.identifier


class TransportGetOptions(PolymorphicModel): ...


class TransportPlaceOptions(PolymorphicModel): ...


class HamiltonCOREGripper(TransportBase):
    class Meta:
        verbose_name = "Hamilton CORE Gripper"
        verbose_name_plural = "Hamilton CORE Grippers"

    gripper_labware_id = models.CharField(max_length=100)


class HamiltonCOREGripperGetOptions(TransportGetOptions):
    check_plate_exists = models.BooleanField()

    def __str__(self) -> str:
        return f"check_plate_exists:{self.check_plate_exists}"


class HamiltonCOREGripperPlaceOptions(TransportPlaceOptions):
    check_plate_exists = models.BooleanField()

    def __str__(self) -> str:
        return f"check_plate_exists:{self.check_plate_exists}"


class HamiltonInternalPlateGripper(TransportBase): ...


class HamiltonInternalPlateGripperGetOptions(TransportGetOptions):
    grip_mode = models.CharField(
        max_length=20,
        choices=(
            ("GripOnShortSide", "Grip On Short Side"),
            ("GripOnLongSide", "Grip On Long Side"),
        ),
    )
    movement = models.CharField(
        max_length=20,
        choices=(
            ("Carrier", "Carrier"),
            ("Complex", "Complex"),
        ),
    )
    retract_distance = models.FloatField()
    liftup_height = models.FloatField()
    labware_orientation = models.CharField(
        max_length=20,
        choices=(
            ("NegativeYAxis", "Negative Y Axis"),
            ("PositiveXAxis", "Positive X Axis"),
            ("PositiveYAxis", "Positive Y Axis"),
            ("NegativeXAxis", "Negative X Axis"),
        ),
    )
    inverse_grip = models.BooleanField()

    def __str__(self) -> str:
        return f"grip_mode:{self.grip_mode}; movement:{self.movement}; retract_distance:{self.retract_distance}; liftup_height:{self.liftup_height}; labware_orientation:{self.labware_orientation}; inverse_grip:{self.inverse_grip}"


class HamiltonInternalPlateGripperPlaceOptions(TransportPlaceOptions):
    movement = models.CharField(
        max_length=20,
        choices=(
            ("Carrier", "Carrier"),
            ("Complex", "Complex"),
        ),
    )
    retract_distance = models.FloatField()
    liftup_height = models.FloatField()
    labware_orientation = models.CharField(
        max_length=20,
        choices=(
            ("NegativeYAxis", "Negative Y Axis"),
            ("PositiveXAxis", "Positive X Axis"),
            ("PositiveYAxis", "Positive Y Axis"),
            ("NegativeXAxis", "Negative X Axis"),
        ),
    )

    def __str__(self) -> str:
        return f"movement:{self.movement}; retract_distance:{self.retract_distance}; liftup_height:{self.liftup_height}; labware_orientation:{self.labware_orientation}"


class VantageTrackGripper(TransportBase): ...


class VantageTrackGripperGetOptions(TransportGetOptions):
    park_labware_id = models.CharField(max_length=100, blank=True)
    taught_path_name = models.CharField(max_length=100)
    path_execution_time = models.FloatField()
    labware_orientation = models.CharField(
        max_length=20,
        choices=(
            ("NegativeYAxis", "Negative Y Axis"),
            ("PositiveXAxis", "Positive X Axis"),
            ("PositiveYAxis", "Positive Y Axis"),
            ("NegativeXAxis", "Negative X Axis"),
        ),
    )
    coordinated_movement = models.BooleanField()

    def __str__(self) -> str:
        return f"park_labware_id:{self.park_labware_id}; taught_path_name:{self.taught_path_name}; path_execution_time:{self.path_execution_time}; labware_orientation:{self.labware_orientation}; coordinated_movement:{self.coordinated_movement}"


class VantageTrackGripperPlaceOptions(TransportPlaceOptions):
    park_labware_id = models.CharField(max_length=100, blank=True)
    taught_path_name = models.CharField(max_length=100)
    path_execution_time = models.FloatField()
    coordinated_movement = models.BooleanField()

    def __str__(self) -> str:
        return f"park_labware_id:{self.park_labware_id}; taught_path_name:{self.taught_path_name}; path_execution_time:{self.path_execution_time}; coordinated_movement:{self.coordinated_movement}"
