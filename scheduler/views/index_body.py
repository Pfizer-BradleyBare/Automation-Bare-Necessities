from django.http import HttpRequest
from django.shortcuts import render

from .index_context import IndexContextView


class IndexBodyView(IndexContextView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "scheduler/index_body.html",
            self.get_context_data(),
        )
