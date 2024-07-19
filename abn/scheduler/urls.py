from django.urls import path

from . import views

urlpatterns = [
    path("gantt_chart", views.gantt_chart, name="gantt_chart"),
    path("method_queue", views.method_queue, name="method_queue"),
    path("test_method", views.test_method, name="test_method"),
    path("queue_method", views.queue_method, name="queue_method"),
    path(
        "queue_method_success",
        views.queue_method_success,
        name="queue_method_success",
    ),
]
