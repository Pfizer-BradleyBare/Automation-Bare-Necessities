import datetime

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone

from method.models import ExecutingMethod

from .queue_method_dashboard_context import QueueMethodDashboardContextView


class QueueMethodDashboardView(QueueMethodDashboardContextView):
    def get(self, request: HttpRequest, filename: str):

        return render(
            request,
            "scheduler/queue_method_dashboard.html",
            self.get_context_data(filename=filename),
        )

    def post(self, request: HttpRequest, filename: str):
        queued_method = ExecutingMethod.objects.get(file__icontains=filename)

        queued_method.emails = request.POST["input-emails"]
        queued_method.phone_numbers = request.POST["input-phone-numbers"]
        queued_method.desired_completion_time = datetime.datetime.strptime(
            request.POST["input-completion-time"],
            "%Y-%m-%dT%H:%M",
        ).astimezone(timezone.get_current_timezone())

        queued_method.save()

        return redirect("scheduler:queue_method_dashboard", filename)
