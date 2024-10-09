from django.contrib import admin

from .models.user_method import ExecutingMethodWorkbook, TestingMethodWorkbook

admin.site.register(TestingMethodWorkbook)
admin.site.register(ExecutingMethodWorkbook)
