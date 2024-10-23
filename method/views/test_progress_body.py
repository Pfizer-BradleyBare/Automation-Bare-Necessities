from django.http import HttpRequest
from django.shortcuts import render

from .test_progress_context import TestProgressContextView


class TestProgressBodyView(TestProgressContextView):
    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "method/test_progress_body.html",
            self.get_context_data(filename=filename),
        )
