from django.contrib.admin import ModelAdmin

from hal.admin import hal_admin

from .forms import TransportableDeckLocationConfigForm, TransportableDeckLocationForm
from .models import (
    NonTransportableDeckLocation,
    TransportableDeckLocation,
    TransportableDeckLocationConfig,
)


class TransportableDeckLocationConfigAdmin(ModelAdmin):
    form = TransportableDeckLocationConfigForm

class TransportableDeckLocationAdmin(ModelAdmin):
    form = TransportableDeckLocationForm


hal_admin.register(NonTransportableDeckLocation)
hal_admin.register(TransportableDeckLocation,TransportableDeckLocationAdmin)
hal_admin.register(
    TransportableDeckLocationConfig,
    TransportableDeckLocationConfigAdmin,
)
