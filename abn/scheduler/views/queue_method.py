from django.http.request import HttpRequest
from django.shortcuts import redirect, render

from .queue_method_success import queue_method_success


def queue_method(request: HttpRequest):
    context = {}
    try:
        emails = [
            email for email in request.POST["input-emails"].split(",") if email != ""
        ]
        phone_numbers = [
            phone_number
            for phone_number in request.POST["input-phone-numbers"].split(",")
            if phone_number != ""
        ]
        if len(emails) + len(phone_numbers) > 0:
            return redirect(queue_method_success)

    except KeyError:
        ...

    return render(request, "scheduler/queue_method.html", context)
