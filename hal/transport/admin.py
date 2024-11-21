from typing import Any

from django.contrib.admin import ModelAdmin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest

from hal.admin import hal_admin
from hal.backend.models.hamilton import HamiltonBackendBase

from .models.hamilton import (
    HamiltonCOREGripper,
    HamiltonCOREGripperPickupOptions,
    HamiltonCOREGripperPlaceOptions,
    # HamiltonInternalPlateGripperComplexMovement,
    # HamiltonInternalPlateGripperComplexMovementPickupOptions,
    # HamiltonInternalPlateGripperComplexMovementPlaceOptions,
    # HamiltonInternalPlateGripperSimpleMovement,
    # HamiltonInternalPlateGripperSimpleMovementPickupOptions,
    # HamiltonInternalPlateGripperSimpleMovementPlaceOptions,
    # HamiltonVantageTrackGripperTaughtMovement,
    # HamiltonVantageTrackGripperTaughtMovementPickupOptions,
    # HamiltonVantageTrackGripperTaughtMovementPlaceOptions,
)


class HamiltonBackendAdmin(ModelAdmin):
    def formfield_for_foreignkey(
        self,
        db_field: ForeignKey[Any],
        request: HttpRequest | None,
        **kwargs: Any,
    ) -> ModelChoiceField | None:
        if db_field.name == "backend":
            kwargs["queryset"] = HamiltonBackendBase.objects

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


hal_admin.register(HamiltonCOREGripper, HamiltonBackendAdmin)
hal_admin.register(HamiltonCOREGripperPickupOptions)
hal_admin.register(HamiltonCOREGripperPlaceOptions)
# hal_admin.register(HamiltonInternalPlateGripperSimpleMovement, HamiltonBackendAdmin)
# hal_admin.register(HamiltonInternalPlateGripperSimpleMovementPickupOptions)
# hal_admin.register(HamiltonInternalPlateGripperSimpleMovementPlaceOptions)
# hal_admin.register(HamiltonInternalPlateGripperComplexMovement, HamiltonBackendAdmin)
# hal_admin.register(HamiltonInternalPlateGripperComplexMovementPickupOptions)
# hal_admin.register(HamiltonInternalPlateGripperComplexMovementPlaceOptions)
# hal_admin.register(HamiltonVantageTrackGripperTaughtMovement, HamiltonBackendAdmin)
# hal_admin.register(HamiltonVantageTrackGripperTaughtMovementPickupOptions)
# hal_admin.register(HamiltonVantageTrackGripperTaughtMovementPlaceOptions)
