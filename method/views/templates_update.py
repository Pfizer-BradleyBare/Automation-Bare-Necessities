from django.http import HttpRequest, HttpResponse

from abn.views import NavbarView


class TemplatesUpdateView(NavbarView):
    def get(self, request: HttpRequest):

        return HttpResponse("Update")
