from django.http import HttpRequest, HttpResponse

from abn.views import NavbarView


class TemplatesMethodView(NavbarView):
    def get(self, request: HttpRequest, method: str):

        return HttpResponse(method)
