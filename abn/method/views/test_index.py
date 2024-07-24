from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView


class TestIndexView(NavbarView):
    def get(self, request: HttpRequest, filename: str = ""):
        return render(request, "method/test_index.html", self.get_context_data())
