from dal import autocomplete
from django import forms

from .models import TransportableDeckLocationConfig


class TransportableDeckLocationConfigForm(forms.ModelForm):
    class Meta:
        model = TransportableDeckLocationConfig
        fields = "__all__"
        widgets = {
            "pickup_options": autocomplete.ModelSelect2(
                url="hal.transport:transport-pickup-options-autocomplete",
                forward=["transport_device"],
                attrs={"data-minimumResultsForSearch": "999", "data-width": "auto"},
            ),
            "place_options": autocomplete.ModelSelect2(
                url="hal.transport:transport-place-options-autocomplete",
                forward=["transport_device"],
                attrs={"data-minimumResultsForSearch": "999", "data-width": "auto"},
            ),
        }
