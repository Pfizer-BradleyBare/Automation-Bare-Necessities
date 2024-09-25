import re

from django.http import HttpRequest
from django.shortcuts import redirect, render

from method.models import ExecutingMethod

from .queue_method_dashboard_context import QueueMethodDashboardContextView


class QueueMethodDashboardAbortView(QueueMethodDashboardContextView):
    def get_context_data(self, **kwargs) -> dict:
        def regex_escape_fixed_string(string):
            "Escape fixed string for regex"
            return re.sub(r"[][(){}?*+.^$]", lambda m: "\\" + m.group(), string)

        return super().get_context_data(**kwargs) | {
            "regex_filename": regex_escape_fixed_string(kwargs.get("filename")),
        }

    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "scheduler/queue_method_dashboard_abort.html",
            self.get_context_data(filename=filename),
        )

    def post(self, request: HttpRequest, filename: str):

        queued_method = ExecutingMethod.objects.get(file__icontains=filename)
        queued_method.state = "Aborted"
        queued_method.save()

        return redirect(
            "scheduler:queue_method_dashboard",
            filename,
        )
