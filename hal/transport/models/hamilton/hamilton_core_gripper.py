from __future__ import annotations

from typing import ClassVar, cast

from django.db import models
from plh.hamilton_venus.HSLLabwrAccess import (
    AbsolutePositionValuesGetForLabwareID,
    AbsolutePositionValuesSetForLabwareID,
)

from hal.layout_item.models import LoadedLayoutItem
from hal.layout_item.models.hamilton import HamiltonLayoutItem

from ..transport_base import (
    TransportBase,
    TransportPickupOptionsBase,
    TransportPlaceOptionsBase,
)


class HamiltonCOREGripper(TransportBase):
    gripper_labware_id = models.CharField(max_length=100)

    _max_grip_depth: ClassVar[float] = 40

    class Meta:
        verbose_name = "Hamilton CORE Gripper"
        verbose_name_plural = "Hamilton CORE Grippers"

    def transport_time(
        self,
        source: LoadedLayoutItem,
        destination: LoadedLayoutItem,
    ) -> float:
        return 0

    def assert_transport(self, source: LoadedLayoutItem, destination: LoadedLayoutItem):
        _, grip_height = self.compute_grip_height(source)

        if not isinstance(source.layout_item, HamiltonLayoutItem):
            raise ValueError("Source is not a hamilton compatible layout item.")

        if not isinstance(destination.layout_item, HamiltonLayoutItem):
            raise ValueError("Destination is not a hamilton compatible layout item.")

        if grip_height is None:
            ValueError(
                "No acceptable grip heights were found for the transport device '{self}'",
            )

        return super().assert_transport(source, destination)

    def transport(self, source: LoadedLayoutItem, destination: LoadedLayoutItem):
        from hal.carrier_location.models import TransportableCarrierLocationConfig

        self.assert_transport(source, destination)

        backend = self.backend.get_plh_backend()

        source_labware_id = cast(
            HamiltonLayoutItem,
            source.layout_item,
        ).venus_labware_id

        destination_labware_id = cast(
            HamiltonLayoutItem,
            destination.layout_item,
        ).venus_labware_id

        command = AbsolutePositionValuesGetForLabwareID.Command(
            options=[
                AbsolutePositionValuesGetForLabwareID.Options(
                    LabwareID=source_labware_id,
                ),
                AbsolutePositionValuesGetForLabwareID.Options(
                    LabwareID=destination_labware_id,
                ),
            ],
        )
        backend.execute(command)
        backend.wait(command)
        response = backend.acknowledge(
            command,
            AbsolutePositionValuesGetForLabwareID.Response,
        )
        source_initial_position, destinition_initial_position = (
            response.LabwarePositions
        )
        # get the current virtual positions so we can reset after transport

        command = AbsolutePositionValuesSetForLabwareID.Command(
            options=[
                AbsolutePositionValuesSetForLabwareID.Options(
                    LabwareID=source_labware_id,
                    XPosition=source_initial_position.XPosition,
                    YPosition=source_initial_position.YPosition,
                    ZPosition=source_initial_position.ZPosition
                    + source.z_height_above_base,
                    ZRotation=source_initial_position.ZRotation,
                ),
            ],
        )
        backend.execute(command)
        backend.wait(command)
        backend.acknowledge(command, AbsolutePositionValuesSetForLabwareID.Response)

        command = AbsolutePositionValuesSetForLabwareID.Command(
            options=[
                AbsolutePositionValuesSetForLabwareID.Options(
                    LabwareID=destination_labware_id,
                    XPosition=destinition_initial_position.XPosition,
                    YPosition=destinition_initial_position.YPosition,
                    ZPosition=destinition_initial_position.ZPosition
                    + destination.height_from_base,
                    ZRotation=destinition_initial_position.ZRotation,
                ),
            ],
        )
        backend.execute(command)
        backend.wait(command)
        backend.acknowledge(command, AbsolutePositionValuesSetForLabwareID.Response)
        # move the labware virtually into the correct space first. Since labware can be stacked

        source_config = TransportableCarrierLocationConfig.objects.filter(
            transportablecarrierlocation=source.layout_item.carrier_location,
            transport_device=self,
        )

        destination_config = TransportableCarrierLocationConfig.objects.filter(
            transportablecarrierlocation=destination.layout_item.carrier_location,
            transport_device=self,
        )

        _, grip_height = cast(tuple[None, float], self.compute_grip_height(source))

        grip_labware = source.layout_item.labware

        command = AbsolutePositionValuesSetForLabwareID.Command(
            options=[
                AbsolutePositionValuesSetForLabwareID.Options(
                    LabwareID=source_labware_id,
                    XPosition=source_initial_position.XPosition,
                    YPosition=source_initial_position.YPosition,
                    ZPosition=source_initial_position.ZPosition,
                    ZRotation=source_initial_position.ZRotation,
                ),
            ],
        )
        backend.execute(command)
        backend.wait(command)
        backend.acknowledge(command, AbsolutePositionValuesSetForLabwareID.Response)

        command = AbsolutePositionValuesSetForLabwareID.Command(
            options=[
                AbsolutePositionValuesSetForLabwareID.Options(
                    LabwareID=destination_labware_id,
                    XPosition=destinition_initial_position.XPosition,
                    YPosition=destinition_initial_position.YPosition,
                    ZPosition=destinition_initial_position.ZPosition,
                    ZRotation=destinition_initial_position.ZRotation,
                ),
            ],
        )
        backend.execute(command)
        backend.wait(command)
        backend.acknowledge(command, AbsolutePositionValuesSetForLabwareID.Response)
        # Reset the labware to the initial deck position.


class HamiltonCOREGripperPickupOptions(TransportPickupOptionsBase):
    transport_device = HamiltonCOREGripper.__name__

    grip_force = models.CharField(
        max_length=25,
        choices=[
            ("Grip Force 0", "Grip Force 0"),
            ("Grip Force 1", "Grip Force 1"),
            ("Grip Force 2", "Grip Force 2"),
            ("Grip Force 3", "Grip Force 3"),
            ("Grip Force 4", "Grip Force 4"),
            ("Grip Force 5", "Grip Force 5"),
            ("Grip Force 6", "Grip Force 6"),
            ("Grip Force 7", "Grip Force 7"),
            ("Grip Force 8", "Grip Force 8"),
            ("Grip Force 9", "Grip Force 9"),
        ],
        default="Grip Force 5",
    )
    grip_speed = models.FloatField(default=277.8)
    z_speed = models.FloatField(default=128.7)
    check_plate_exists = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "grip_force",
            "grip_speed",
            "z_speed",
            "check_plate_exists",
        )

    def __str__(self) -> str:
        return f"grip_force:{self.grip_force}; grip_speed:{self.grip_speed}; z_speed:{self.z_speed}; check_plate_exists:{self.check_plate_exists}"

    def test_options_equality(
        self: HamiltonCOREGripperPickupOptions,
        value: object,
    ) -> bool:
        if not isinstance(value, HamiltonCOREGripperPickupOptions):
            return False

        return True


class HamiltonCOREGripperPlaceOptions(TransportPlaceOptionsBase):
    transport_device = HamiltonCOREGripper.__name__

    x_acceleration_level = models.CharField(
        max_length=25,
        choices=(
            ("Level 1", "Level 1"),
            ("Level 2", "Level 2"),
            ("Level 3", "Level 3"),
            ("Level 4", "Level 4"),
            ("Level 5", "Level 5"),
        ),
        default="Level 4",
    )
    z_speed = models.FloatField(default=128.7)
    plate_press_on_distance = models.FloatField(default=1)
    check_plate_exists = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "x_acceleration_level",
            "z_speed",
            "plate_press_on_distance",
            "check_plate_exists",
        )

    def __str__(self) -> str:
        return f"x_acceleration_level:{self.x_acceleration_level}; z_speed:{self.z_speed}; plate_press_on_distance:{self.plate_press_on_distance}; check_plate_exists:{self.check_plate_exists}"

    def test_options_equality(
        self: HamiltonCOREGripperPlaceOptions,
        value: object,
    ) -> bool:
        if not isinstance(value, HamiltonCOREGripperPlaceOptions):
            return False

        return True
