from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView


class TestProgressView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        filename = kwargs.get("filename")

        try:
            context = {
                "filename": filename,
                "progress": 1,
                "rows": [],
            }
        except ObjectDoesNotExist:
            context = {}

        return super().get_context_data() | context

    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "method/test_progress.html",
            self.get_context_data(filename=filename),
        )
