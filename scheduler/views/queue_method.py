import datetime
from pathlib import Path

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone

from abn.views import NavbarView
from method.models.user_method import ExecutingMethodWorkbook


class QueueMethodView(NavbarView):
    def get(self, request: HttpRequest):
        return render(
            request,
            "scheduler/queue_method.html",
            self.get_context_data(),
        )

    def post(self, request: HttpRequest):

        raw_emails = request.POST["input-emails"]
        raw_phone_numbers = request.POST["input-phone-numbers"]
        raw_completion_time = request.POST["input-completion-time"]
        raw_method_file = request.FILES["input-method-file"]
        method_file_name = Path(raw_method_file.name).stem

        if not ExecutingMethodWorkbook.objects.filter(
            file__icontains=method_file_name,
        ).exists():
            ExecutingMethodWorkbook(
                emails=raw_emails,
                phone_numbers=raw_phone_numbers,
                desired_completion_time=datetime.datetime.strptime(
                    raw_completion_time,
                    "%Y-%m-%dT%H:%M",
                ).astimezone(timezone.get_current_timezone()),
                file=raw_method_file,
            ).save()

            return redirect("scheduler:queue_method_success")

        return redirect("scheduler:queue_method_error")
