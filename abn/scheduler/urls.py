from django.urls import path

from . import views

app_name = "scheduler"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("body", views.IndexBodyView.as_view(), name="index_body"),
    path("queue", views.QueueIndexView.as_view(), name="queue"),
    path("queue/method", views.QueueMethodView.as_view(), name="queue_method"),
    path(
        "queue/method/success",
        views.QueueMethodSuccessView.as_view(),
        name="queue_method_success",
    ),
    path(
        "queue/method/error",
        views.QueueMethodErrorView.as_view(),
        name="queue_method_error",
    ),
    path(
        "queue/method/<str:filename>/",
        views.QueueMethodDashboardView.as_view(),
        name="queue_method_dashboard",
    ),
    path(
        "queue/method/<str:filename>/body",
        views.QueueMethodDashboardBodyView.as_view(),
        name="queue_method_dashboard_body",
    ),
    path(
        "queue/method/<str:filename>/abort",
        views.QueueMethodDashboardAbortView.as_view(),
        name="queue_method_dashboard_abort",
    ),
    path(
        "queue/method/<str:filename>/edit",
        views.QueueMethodDashboardEditView.as_view(),
        name="queue_method_dashboard_edit",
    ),
    path(
        "queue/method/<str:filename>/edit/download",
        views.QueueMethodDashboardEditDownloadView.as_view(),
        name="queue_method_dashboard_edit_download",
    ),
    path(
        "queue/method/<str:filename>/pause",
        views.QueueMethodDashboardPauseView.as_view(),
        name="queue_method_dashboard_pause",
    ),
    path(
        "queue/method/<str:filename>/resume",
        views.QueueMethodDashboardResumeView.as_view(),
        name="queue_method_dashboard_resume",
    ),
]
