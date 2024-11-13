from django.contrib.admin import ModelAdmin

from hal.admin import hal_admin

from .forms import TransportableDeckLocationConfigForm
from .models import (
    NonTransportableDeckLocation,
    TransportableDeckLocation,
    TransportableDeckLocationConfig,
)


class TransportableDeckLocationConfigAdmin(ModelAdmin):
    form = TransportableDeckLocationConfigForm


hal_admin.register(NonTransportableDeckLocation)
hal_admin.register(TransportableDeckLocation)
hal_admin.register(
    TransportableDeckLocationConfig,
    TransportableDeckLocationConfigAdmin,
)
