from django.urls import path

from .admin import plh_admin

urlpatterns = [
    path("", plh_admin.urls, name="plh_admin"),
]
