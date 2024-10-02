from django.contrib import admin

from .models import ExecutingMethodWorkbook, TestingMethodWorkbook

admin.site.register(TestingMethodWorkbook)
admin.site.register(ExecutingMethodWorkbook)
