from django.urls import path

from . import views

app_name = "trace"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("body", views.IndexBodyView.as_view(), name="body"),
]
