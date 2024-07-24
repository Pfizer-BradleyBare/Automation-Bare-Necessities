from django.http import HttpRequest
from django.shortcuts import redirect, render

from abn.views import NavbarView


class TestIndexView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        return super().get_context_data(**kwargs) | {
            "header": "Test Method",
            "description": 'Will test an ABN method containing both a "Method" and a "Worklist" sheet. Once testing completes successfully you will be able to download a preparation list and queue the method for execution.',
            "body": "",
        }

    def get(self, request: HttpRequest):
        return render(
            request,
            "method/test_index.html",
            self.get_context_data(),
        )

    def post(self, request: HttpRequest):
        return redirect("method:progress", "ttt")
