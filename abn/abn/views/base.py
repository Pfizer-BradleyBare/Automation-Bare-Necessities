from __future__ import annotations

from django.http import HttpRequest, HttpResponseNotFound
from django.views.generic import View


class BaseView(View):
    def get_context_data(self, **kwargs) -> dict:
        return {}

    def get(self, request: HttpRequest):
        return HttpResponseNotFound("No endpoint defined")

    def post(self, request: HttpRequest):
        return HttpResponseNotFound("No endpoint defined")
