from django.http import HttpRequest
from django.shortcuts import render

from abn.views import NavbarView
from block.models.meta_data import Author, Category, DocumentNumber, Modality, Project
from method.models import TemplateMethodWorkbook


class TemplatesIndexView(NavbarView):
    def get_context_data(self, **kwargs) -> dict:
        context = {}

        rows = []
        for method in TemplateMethodWorkbook.objects.all():
            name = str(method)
            authors = ", ".join(
                [
                    str(item.meta_data_text)
                    for item in Author.objects.filter(method=method).all()
                ],
            )
            categories = ", ".join(
                [
                    str(item.meta_data_text)
                    for item in Category.objects.filter(method=method).all()
                ],
            )
            document_numbers = ", ".join(
                [
                    str(item.meta_data_text)
                    for item in DocumentNumber.objects.filter(method=method).all()
                ],
            )
            modalities = ", ".join(
                [
                    str(item.meta_data_text)
                    for item in Modality.objects.filter(method=method).all()
                ],
            )
            projects = ", ".join(
                [
                    str(item.meta_data_text)
                    for item in Project.objects.filter(method=method).all()
                ],
            )

            rows.append(
                [name, authors, document_numbers, categories, modalities, projects],
            )

        context["rows"] = rows

        return super().get_context_data(**kwargs) | context

    def get(self, request: HttpRequest):
        return render(
            request,
            "method/templates_index.html",
            self.get_context_data(),
        )
