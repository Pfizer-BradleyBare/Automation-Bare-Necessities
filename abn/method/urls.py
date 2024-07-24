from django.urls import path

from . import views

app_name = "method"

urlpatterns = [
    path("test/", views.TestIndexView.as_view(), name="test"),
    path(
        "test/<str:filename>/",
        views.TestIndexView.as_view(),
    ),
]
