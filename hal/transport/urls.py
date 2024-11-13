from django.urls import path

from .views import TransportPickupOptionsAutocomplete, TransportPlaceOptionsAutocomplete

app_name = "hal.transport"

urlpatterns = [
    path(
        "transport-pickup-options-autocomplete",
        TransportPickupOptionsAutocomplete.as_view(),
        name="transport-pickup-options-autocomplete",
    ),
    path(
        "transport-place-options-autocomplete",
        TransportPlaceOptionsAutocomplete.as_view(),
        name="transport-place-options-autocomplete",
    ),
]
