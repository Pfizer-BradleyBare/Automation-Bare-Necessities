from abn_config.admin import config_admin

from .models import (
    NonTransportableDeckLocation,
    TransportableDeckLocation,
    TransportConfig,
)

config_admin.register(NonTransportableDeckLocation)
config_admin.register(TransportableDeckLocation)
config_admin.register(TransportConfig)
