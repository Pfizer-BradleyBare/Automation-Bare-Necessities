from django.http.request import HttpRequest
from django.shortcuts import render


def test_method(request: HttpRequest):
    return render(request, "method/test/index.html", {})
