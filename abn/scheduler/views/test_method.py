from django.http.request import HttpRequest
from django.shortcuts import render


def test_method(request: HttpRequest):
    return render(request, "scheduler/test_method.html", {})
