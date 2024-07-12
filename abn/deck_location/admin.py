from django.contrib import admin

from .models import (
    NonTransportableDeckLocation,
    TransportableDeckLocation,
    TransportConfig,
)

admin.site.register(NonTransportableDeckLocation)
admin.site.register(TransportableDeckLocation)
admin.site.register(TransportConfig)
