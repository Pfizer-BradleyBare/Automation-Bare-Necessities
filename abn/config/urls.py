from django.urls import path

from .admin import config_admin

urlpatterns = [
    path("", config_admin.urls, name="config_admin"),
]
