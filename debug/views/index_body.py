from django.http import HttpRequest
from django.shortcuts import render

from .index_context import IndexContextView


class IndexBodyView(IndexContextView):
    def post(self, request: HttpRequest):

        return render(
            request,
            "trace/index_body.html",
            self.get_context_data(
                log_source=request.POST["input-log-source"],
                log_level=request.POST["input-log-level"],
                meta_info=request.POST["input-extra-info"],
                debug_message=request.POST["input-debug-message"],
            ),
        )
