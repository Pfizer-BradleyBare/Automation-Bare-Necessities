from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class TestProgressBodyView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        filename = kwargs.get("filename")

        try:

            context = {
                "filename": filename,
                "progress": l.pop(0) * 10,
                "rows": [],
            }
        except ObjectDoesNotExist:
            context = {}

        return super().get_context_data() | context

    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "method/test_progress_body.html",
            self.get_context_data(filename=filename),
        )
