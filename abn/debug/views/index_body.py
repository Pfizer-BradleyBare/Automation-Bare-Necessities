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
                method_name=request.POST["input-method-name"],
                device_identifier=request.POST["input-device-identifier"],
                debug_message=request.POST["input-debug-message"],
            ),
        )
