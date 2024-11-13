from dal import autocomplete
from django.apps import apps

from hal.transport.models import TransportBase

from .models import TransportPickupOptionsBase, TransportPlaceOptionsBase


class TransportPickupOptionsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        transport_device = self.forwarded.get("transport_device")

        if transport_device:
            transport_device_model_name = type(
                TransportBase.objects.filter(pk=transport_device).get(),
            ).__name__

            options_model_name = f"{transport_device_model_name}PickupOptions"

            model = apps.get_model(
                app_label="transport",
                model_name=options_model_name,
            )
            return model.objects.all()

        return TransportPickupOptionsBase.objects.none()


class TransportPlaceOptionsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        transport_device = self.forwarded.get("transport_device")

        if transport_device:
            transport_device_model_name = type(
                TransportBase.objects.filter(pk=transport_device).get(),
            ).__name__

            options_model_name = f"{transport_device_model_name}PlaceOptions"

            model = apps.get_model(
                app_label="transport",
                model_name=options_model_name,
            )
            return model.objects.all()

        return TransportPlaceOptionsBase.objects.none()
