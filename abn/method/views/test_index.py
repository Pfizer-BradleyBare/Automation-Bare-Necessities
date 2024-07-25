from django.http import HttpRequest
from django.shortcuts import redirect, render

from abn.views import NavbarView


class TestIndexView(NavbarView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "method/test_index.html",
            self.get_context_data(),
        )

    def post(self, request: HttpRequest):
        return redirect("method:progress", "ttt")
