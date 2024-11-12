from typing import Any

from django.contrib.admin import ModelAdmin
from django.http import HttpRequest

from hal.admin import hal_admin

from .models import NonPipettableLabware, PipettableLabware


class DisableIdentifierAdmin(ModelAdmin):
    def get_readonly_fields(
        self,
        request: HttpRequest,
        obj: Any | None = ...,
    ) -> list[str] | tuple[Any, ...]:
        if obj:
            return ["identifier"]
        return []


hal_admin.register(NonPipettableLabware, DisableIdentifierAdmin)
hal_admin.register(PipettableLabware, DisableIdentifierAdmin)
