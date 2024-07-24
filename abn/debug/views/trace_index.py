from django.http import HttpRequest
from django.shortcuts import render

from .trace_context import TraceContextView


class IndexView(TraceContextView):
    def get(self, request: HttpRequest):
        return render(request, "trace/index.html", self.get_context_data())
