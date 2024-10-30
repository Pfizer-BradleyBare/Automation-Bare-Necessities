from django.db import models

from solution.models.component_base import ComponentBase

from .container_base import ContainerBase


class SolutionContainer(ContainerBase):
    solution = models.ForeignKey(to=ComponentBase, on_delete=models.CASCADE)
