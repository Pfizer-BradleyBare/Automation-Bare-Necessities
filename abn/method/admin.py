from django.contrib import admin

from .models import TestMessage, TestMethod

admin.site.register(TestMessage)
admin.site.register(TestMethod)
