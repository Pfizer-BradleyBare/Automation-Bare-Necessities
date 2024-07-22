from django.urls import path

from . import views

urlpatterns = [path("trace", views.trace, name="trace")]
