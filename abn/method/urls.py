from django.urls import path

from . import views

app_name = "method"

urlpatterns = [
    path("test/", views.TestIndexView.as_view(), name="test"),
    path(
        "test/<str:filename>/",
        views.TestProgressView.as_view(),
        name="progress",
    ),
    path(
        "test/body/<str:filename>/",
        views.TestProgressBodyView.as_view(),
        name="progress_body",
    ),
    path(
        "test/<str:filename>/preparation_list",
        views.TestPreparationListView.as_view(),
        name="preparation_list",
    ),
]
