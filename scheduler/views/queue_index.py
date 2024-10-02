from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView
from method.models import ExecutingMethodWorkbook


class QueueIndexView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        context = {
            "rows": sorted(
                [str(m) for m in ExecutingMethodWorkbook.objects.all()],
                key=lambda x: x.lower(),
            ),
        }
        return super().get_context_data() | context

    def get(self, request: HttpRequest):
        return render(
            request,
            "scheduler/queue_index.html",
            self.get_context_data(),
        )
