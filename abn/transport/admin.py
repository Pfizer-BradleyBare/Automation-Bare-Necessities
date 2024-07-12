from django.contrib import admin

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

admin.site.register(VantageTrackGripper)
admin.site.register(VantageTrackGripperGetOptions)
admin.site.register(VantageTrackGripperPlaceOptions)
admin.site.register(HamiltonCOREGripper)
admin.site.register(HamiltonCOREGripperGetOptions)
admin.site.register(HamiltonCOREGripperPlaceOptions)
admin.site.register(HamiltonInternalPlateGripper)
admin.site.register(HamiltonInternalPlateGripperGetOptions)
admin.site.register(HamiltonInternalPlateGripperPlaceOptions)
