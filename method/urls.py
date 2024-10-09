from django.urls import path

from . import views

app_name = "method"

urlpatterns = [
    path("templates/", views.TemplatesIndexView.as_view(), name="templates"),
    path(
        "templates/update",
        views.TemplatesBlankView.as_view(),
        name="templates_update",
    ),
    path("templates/blank", views.TemplatesBlankView.as_view(), name="templates_blank"),
    path(
        "templates/<str:method>",
        views.TemplatesMethodView.as_view(),
        name="templates_method",
    ),
    path("test/", views.TestIndexView.as_view(), name="test"),
    path(
        "test/<str:filename>/",
        views.TestProgressView.as_view(),
        name="progress",
    ),
    path(
        "test/<str:filename>/body",
        views.TestProgressBodyView.as_view(),
        name="progress_body",
    ),
    path(
        "test/<str:filename>/preparation_list",
        views.TestPreparationListView.as_view(),
        name="progress_preparation_list",
    ),
]
