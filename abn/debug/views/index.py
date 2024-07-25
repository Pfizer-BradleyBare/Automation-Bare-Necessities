from django.http import HttpRequest
from django.shortcuts import render

from .context import ContextView


class IndexView(ContextView):
    def get(self, request: HttpRequest):
        return render(request, "trace/index.html", self.get_context_data())
