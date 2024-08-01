from django.http import HttpRequest
from django.shortcuts import render

from .index_context import IndexContextView


class IndexView(IndexContextView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "scheduler/index.html",
            self.get_context_data(),
        )
