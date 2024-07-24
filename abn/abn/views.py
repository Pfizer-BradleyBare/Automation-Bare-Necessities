from __future__ import annotations

from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View


class BaseView(View):
    def get_context_data(self, **kwargs) -> dict:
        return {}

    def get(self, request: HttpRequest):
        return HttpResponseNotFound("No endpoint defined")

    def post(self, request: HttpRequest):
        return HttpResponseNotFound("No endpoint defined")


class NavbarView(BaseView):
    def get_context_data(self, **kwargs) -> dict:

        context = {"abn_state": "standby"}

        return super().get_context_data(**kwargs) | context


class IndexView(NavbarView):
    def get(self, request: HttpRequest):
        return render(request, "index.html", self.get_context_data())
