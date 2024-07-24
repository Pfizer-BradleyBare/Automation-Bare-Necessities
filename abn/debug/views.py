from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView

from .models import TraceEntry


class TraceContextView(NavbarView):

    def get_context_data(self, **kwargs) -> dict:

        num_objects = 500

        kwargs.setdefault("log_source", "ALL")
        kwargs.setdefault("log_level", "ALL")
        kwargs.setdefault("method_name", "")
        kwargs.setdefault("device_identifier", "")
        kwargs.setdefault("debug_message", "")

        log_source = kwargs.get("log_source")
        log_level = kwargs.get("log_level")
        method_name = kwargs.get("method_name")
        device_identifier = kwargs.get("device_identifier")
        debug_message = kwargs.get("debug_message")

        query = TraceEntry.objects

        if log_source != "ALL":
            query = query.filter(log_source=log_source)
        if log_level != "ALL":
            query = query.filter(log_level=log_level)
        if method_name != "":
            query = query.filter(method__name__icontains=method_name)
        if device_identifier != "":
            query = query.filter(device_identifier__icontains=device_identifier)
        if debug_message != "":
            query = query.filter(message__icontains=debug_message)

        objects = query.all()[:num_objects]

        context = {
            "table_rows": sorted(
                [
                    [
                        object.time_stamp.strftime("%b %d, %Y, %I:%M %p"),
                        object.log_source,
                        object.log_level,
                        object.method.file.name,
                        object.device_identifier,
                        object.message,
                    ]
                    for object in objects
                ],
                key=lambda x: x[0],
            ),
        }

        return super().get_context_data(**kwargs) | context


class IndexView(TraceContextView):
    def get(self, request: HttpRequest):
        return render(request, "debug/trace/index.html", self.get_context_data())


class TraceBodyView(TraceContextView):
    def post(self, request: HttpRequest):

        return render(
            request,
            "debug/trace/trace_body.html",
            self.get_context_data(
                log_source=request.POST["input-log-source"],
                log_level=request.POST["input-log-level"],
                method_name=request.POST["input-method-name"],
                device_identifier=request.POST["input-device-identifier"],
                debug_message=request.POST["input-debug-message"],
            ),
        )
