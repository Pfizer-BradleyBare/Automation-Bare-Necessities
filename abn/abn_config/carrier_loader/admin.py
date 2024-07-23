from abn_config.admin import config_admin

from .models import HamiltonSTARAutoload, HamiltonVantageAutoload

config_admin.register(HamiltonSTARAutoload)
config_admin.register(HamiltonVantageAutoload)
