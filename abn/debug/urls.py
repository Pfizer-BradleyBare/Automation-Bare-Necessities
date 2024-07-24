from django.urls import path

from . import views

app_name = "trace"

urlpatterns = [
    path("", views.TraceIndexView.as_view(), name="index"),
    path("body", views.TraceBodyView.as_view(), name="body"),
]
