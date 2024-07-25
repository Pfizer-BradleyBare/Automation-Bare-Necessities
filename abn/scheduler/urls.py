from django.urls import path

from . import views

app_name = "scheduler"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("body", views.IndexBodyView.as_view(), name="index_body"),
    path("method_queue", views.method_queue.method_queue, name="queue"),
    path("queue_method", views.queue_method.queue_method, name="queue_method"),
    path(
        "queue_method_success",
        views.queue_method_success.queue_method_success,
        name="queue_method_success",
    ),
]
