from django.contrib.admin import ModelAdmin

from hal.admin import hal_admin

from .forms import TransportableCarrierLocationConfigForm, TransportableCarrierLocationForm
from .models import (
    NonTransportableCarrierLocation,
    TransportableCarrierLocation,
    TransportableCarrierLocationConfig,
)


class TransportableCarrierLocationConfigAdmin(ModelAdmin):
    form = TransportableCarrierLocationConfigForm

class TransportableCarrierLocationAdmin(ModelAdmin):
    form = TransportableCarrierLocationForm


hal_admin.register(NonTransportableCarrierLocation)
hal_admin.register(TransportableCarrierLocation,TransportableCarrierLocationAdmin)
hal_admin.register(
    TransportableCarrierLocationConfig,
    TransportableCarrierLocationConfigAdmin,
)
