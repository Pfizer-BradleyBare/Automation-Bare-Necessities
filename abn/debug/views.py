from django.http import HttpRequest
from django.shortcuts import render

from .models import TraceEntry


def trace(request: HttpRequest):
    objects = list(TraceEntry.objects.all())

    context = {
        "rows": sorted(
            [
                [
                    object.time_stamp.strftime("%b %d, %Y, %I:%M %p"),
                    object.level,
                    object.method.name,
                    object.device_identifier,
                    object.message,
                ]
                for object in objects
            ]
            * 500,
            key=lambda x: x[0],
        ),
    }

    return render(request, "debug/trace.html", context)
