from django.contrib import admin

from .models import HamiltonHeaterCooler, HamiltonHeaterShaker

# Register your models here.

admin.site.register(HamiltonHeaterShaker)
admin.site.register(HamiltonHeaterCooler)
