from django.http import HttpRequest, HttpResponse

from abn.views import NavbarView


class QueueMethodDashboardView(NavbarView):
    def get(self, request: HttpRequest, filename: str):
        return HttpResponse(filename)
