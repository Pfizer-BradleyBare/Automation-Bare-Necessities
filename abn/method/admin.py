from django.contrib import admin

from .models import ExecutingMethod, TestingMethod

admin.site.register(TestingMethod)
admin.site.register(ExecutingMethod)
