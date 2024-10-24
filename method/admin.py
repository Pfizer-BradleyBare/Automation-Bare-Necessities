from __future__ import annotations

from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from .models import (
    ExecutingMethodWorkbook,
    TemplateMethodWorkbook,
    TestingMethodWorkbook,
)


class WorkbookAdmin(admin.ModelAdmin):
    def get_readonly_fields(
        self,
        _: HttpRequest,
        obj: Any | None = ...,
    ) -> list[str] | tuple[Any, ...]:
        if obj:
            return ["file"]

        return []

    # Disable being able to change the file after method is created. Protects from major issues down the line caused by changing the method file in admin.


admin.site.register(TestingMethodWorkbook, WorkbookAdmin)
admin.site.register(ExecutingMethodWorkbook, WorkbookAdmin)
admin.site.register(TemplateMethodWorkbook, WorkbookAdmin)
