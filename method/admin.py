from django.contrib import admin

from .models import (
    ExecutingMethodWorkbook,
    TemplateMethodWorkbook,
    TestingMethodWorkbook,
)

admin.site.register(TestingMethodWorkbook)
admin.site.register(ExecutingMethodWorkbook)
admin.site.register(TemplateMethodWorkbook)
