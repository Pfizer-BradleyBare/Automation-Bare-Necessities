from django.urls import path

from . import views

app_name = "abn"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("brand", views.NavbarBrandView.as_view(), name="brand"),
    path("start", views.StartView.as_view(), name="start"),
    path("stop", views.StopView.as_view(), name="stop"),
]
