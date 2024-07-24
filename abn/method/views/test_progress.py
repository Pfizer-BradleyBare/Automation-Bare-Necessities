from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string

from abn.views import NavbarView


class TestProgressView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        kwargs.setdefault("request", None)

        filename = kwargs.get("filename")

        try:
            body_context = {}
        except ObjectDoesNotExist:
            body_context = {}

        body = render_to_string(
            "method/test_progress.html",
            body_context,
            kwargs.get("request"),
        )

        additional_context = {
            "header": "Test Method",
            "description": 'Will test an ABN method containing both a "Method" and a "Worklist" sheet. Once testing completes successfully you will be able to download a preparation list and queue the method for execution.',
            "body": body,
        }

        return super().get_context_data() | additional_context

    def get(self, request: HttpRequest, filename: str):
        return render(
            request,
            "method/test_base.html",
            self.get_context_data(request=request, filename=filename),
        )
