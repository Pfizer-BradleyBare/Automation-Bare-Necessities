from django.http import HttpRequest
from django.shortcuts import redirect, render

from abn.views import NavbarView
from scheduler.models import QueuedMethod


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
        method_file_name = raw_method_file.name

        if not QueuedMethod.objects.filter(file_name=method_file_name).exists():
            QueuedMethod(
                emails=raw_emails,
                phone_numbers=raw_phone_numbers,
                completion_time=raw_completion_time,
                file=raw_method_file,
                file_name=method_file_name,
            ).save()

            return redirect("scheduler:queue_method_success")

        return redirect("scheduler:queue_method_error")
