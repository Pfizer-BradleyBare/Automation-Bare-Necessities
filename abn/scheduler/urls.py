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
]
