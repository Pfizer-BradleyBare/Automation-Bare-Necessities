from django.http import HttpRequest
from django.shortcuts import render

from .models import TraceEntry


def trace(request: HttpRequest):

    num_objects = 500

    if request.method == "POST":
        log_source = request.POST["input-log-source"]
        log_level = request.POST["input-log-level"]
        method_name = request.POST["input-method-name"]
        device_identifier = request.POST["input-device-identifier"]
        debug_message = request.POST["input-debug-message"]

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
            "rows": sorted(
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
        return render(request, "debug/trace/tbody.html", context)
    else:
        objects = TraceEntry.objects.all()[:num_objects]
        context = {
            "rows": sorted(
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
        return render(request, "debug/trace/index.html", context)
