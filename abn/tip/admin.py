from django.contrib import admin

from .models import (
    HamiltonEEFTR1000uL,
    HamiltonEENTR,
    HamiltonEETipStack,
    HamiltonFTR,
    HamiltonNTR,
)

admin.site.register(HamiltonFTR)
admin.site.register(HamiltonNTR)
admin.site.register(HamiltonEETipStack)
admin.site.register(HamiltonEENTR)
admin.site.register(HamiltonEEFTR1000uL)
