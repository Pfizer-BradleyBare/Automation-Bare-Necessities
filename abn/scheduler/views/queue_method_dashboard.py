import datetime

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone

from abn.views import NavbarView
from scheduler.models import QueuedMethod


class QueueMethodDashboardView(NavbarView):
    def get(self, request: HttpRequest, filename: str):
        queued_method = QueuedMethod.objects.get(filename=filename)

        return render(
            request,
            "scheduler/queue_method_dashboard.html",
            self.get_context_data()
            | {
                "state": queued_method.state.lower(),
                "filename": queued_method.filename,
                "progress": 0,
                "start_time": "10 days 24 hours 25 minutes",
                "time_remaining": "10 days 24 hours 25 minutes",
                "emails": queued_method.emails,
                "phone_numbers": queued_method.phone_numbers,
                "completion_time": queued_method.completion_time.astimezone(
                    timezone.get_current_timezone(),
                ).strftime(
                    "%Y-%m-%dT%H:%M",
                ),
            },
        )

    def post(self, request: HttpRequest, filename: str):
        queued_method = QueuedMethod.objects.get(filename=filename)

        queued_method.emails = request.POST["input-emails"]
        queued_method.phone_numbers = request.POST["input-phone-numbers"]
        queued_method.completion_time = datetime.datetime.strptime(
            request.POST["input-completion-time"],
            "%Y-%m-%dT%H:%M",
        ).astimezone(timezone.get_current_timezone())

        queued_method.save()

        return redirect("scheduler:queue_method_dashboard", filename)
