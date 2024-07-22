from django.http import HttpRequest
from django.shortcuts import render


def trace(request: HttpRequest):
    context = {
        "rows": [
            [
                "CRITICAL",
            ]
            for i in range(100)
        ],
    }

    return render(request, "debug/trace.html", context)
