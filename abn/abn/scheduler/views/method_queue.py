from django.http.request import HttpRequest
from django.shortcuts import render


def method_queue(request: HttpRequest):
    return render(request, "scheduler/method_queue.html", {})
