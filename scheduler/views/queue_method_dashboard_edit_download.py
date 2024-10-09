from pathlib import Path

from django.http import FileResponse, HttpRequest

from method.models.user_method import ExecutingMethodWorkbook

from .queue_method_dashboard_context import QueueMethodDashboardContextView


class QueueMethodDashboardEditDownloadView(QueueMethodDashboardContextView):
    def get(self, request: HttpRequest, filename: str):

        queued_method = ExecutingMethodWorkbook.objects.get(file__icontains=filename)

        return FileResponse(
            open(
                Path(queued_method.file.path),
                "rb",
            ),
            as_attachment=True,
            filename=f"{Path(filename).stem}.xlsm",
        )
