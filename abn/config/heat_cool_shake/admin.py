from config.admin import config_admin

from .models import HamiltonHeaterCooler, HamiltonHeaterShaker

# Register your models here.

config_admin.register(HamiltonHeaterShaker)
config_admin.register(HamiltonHeaterCooler)
