from django.http.request import HttpRequest
from django.shortcuts import render


def queue_method_success(request: HttpRequest):
    return render(request, "scheduler/queue_method_success.html", {})
