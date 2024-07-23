from plh_config.admin import config_admin

from .models import (
    HamiltonCOREGripper,
    HamiltonCOREGripperGetOptions,
    HamiltonCOREGripperPlaceOptions,
    HamiltonInternalPlateGripper,
    HamiltonInternalPlateGripperGetOptions,
    HamiltonInternalPlateGripperPlaceOptions,
    VantageTrackGripper,
    VantageTrackGripperGetOptions,
    VantageTrackGripperPlaceOptions,
)

config_admin.register(VantageTrackGripper)
config_admin.register(VantageTrackGripperGetOptions)
config_admin.register(VantageTrackGripperPlaceOptions)
config_admin.register(HamiltonCOREGripper)
config_admin.register(HamiltonCOREGripperGetOptions)
config_admin.register(HamiltonCOREGripperPlaceOptions)
config_admin.register(HamiltonInternalPlateGripper)
config_admin.register(HamiltonInternalPlateGripperGetOptions)
config_admin.register(HamiltonInternalPlateGripperPlaceOptions)
