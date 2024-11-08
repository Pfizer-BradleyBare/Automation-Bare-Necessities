from django.urls import path

from .admin import hal_admin

urlpatterns = [
    path("", hal_admin.urls, name="hal_admin"),
]
