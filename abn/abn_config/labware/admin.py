from abn_config.admin import config_admin

from .models import NonPipettableLabware, PipettableLabware

config_admin.register(NonPipettableLabware)
config_admin.register(PipettableLabware)
