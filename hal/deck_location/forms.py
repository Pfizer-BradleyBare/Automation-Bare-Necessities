
from typing import Any

from django import forms
from django.utils.safestring import SafeText

from .models import TransportableDeckLocationConfig


class DeviceSelect(forms.Select):
    def create_option(self, *args,**kwargs) -> dict[str, Any]:
        option = super().create_option(*args,**kwargs)

        value = option.get("value")

        if value:
            option["attrs"]["data-transport_device"] = type(value.instance).__name__
        else:
            option["attrs"]["data-transport_device"] = None

        return option

    def render(self, *args, **kwargs) -> SafeText:
        html = super().render(*args, **kwargs)

        return html + SafeText(
"""
<script>
function transport_device_change() {
    var transportDeviceSelect = document.getElementById("id_transport_device");
    var pickupOptionsSelect = document.getElementById("id_pickup_options");
    var placeOptionsSelect = document.getElementById("id_place_options");

    var selectedIndex = transportDeviceSelect.selectedIndex
    var selectedOption = transportDeviceSelect.options[selectedIndex]
    var selectedTransportDevice = selectedOption.getAttribute("Data-transport_device")

    pickupOptionsSelect.selectedIndex = 0
    placeOptionsSelect.selectedIndex = 0

    for (let filterIndex = 1; filterIndex < pickupOptionsSelect.options.length; filterIndex++) {
        var filterOption = pickupOptionsSelect.options[filterIndex]
        var filterTransportDevice = filterOption.getAttribute("Data-transport_device")

        if (filterTransportDevice == selectedTransportDevice)
        {
            filterOption.style.display = "block"
        }
        else
        {
            filterOption.style.display = "none"
        }
    }

    for (let filterIndex = 1; filterIndex < placeOptionsSelect.options.length; filterIndex++) {
        var filterOption = placeOptionsSelect.options[filterIndex]
        var filterTransportDevice = filterOption.getAttribute("Data-transport_device")

        if (filterTransportDevice == selectedTransportDevice)
        {
            filterOption.style.display = "block"
        }
        else
        {
            filterOption.style.display = "none"
        }
    }
}
</script>
""")

class OptionsSelect(forms.Select):
    def create_option(self, *args,**kwargs) -> dict[str, Any]:
        option = super().create_option(*args,**kwargs)

        value = option.get("value")

        if value:
            option["attrs"]["data-transport_device"] = value.instance.transport_device
        else:
            option["attrs"]["data-transport_device"] = None

        return option



class TransportableDeckLocationConfigForm(forms.ModelForm):
    class Meta:
        model = TransportableDeckLocationConfig
        fields = "__all__"
        widgets = {
            "transport_device": DeviceSelect(attrs={"onchange":"transport_device_change()"}),
            "pickup_options": OptionsSelect(),
            "place_options": OptionsSelect(),
        }
