from __future__ import annotations

from django.http import HttpRequest
from django.shortcuts import render

from .navbar import NavbarView


class NavbarBrandView(NavbarView):
    def get(self, request: HttpRequest):
        return render(request, "navbar_brand.html", self.get_context_data())
