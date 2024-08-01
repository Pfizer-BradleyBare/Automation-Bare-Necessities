from plh_config.admin import config_admin

from .models import (
    HamiltonEEFTR1000uL,
    HamiltonEENTR,
    HamiltonEETipStack,
    HamiltonFTR,
    HamiltonNTR,
)

config_admin.register(HamiltonFTR)
config_admin.register(HamiltonNTR)
config_admin.register(HamiltonEETipStack)
config_admin.register(HamiltonEENTR)
config_admin.register(HamiltonEEFTR1000uL)
