from django.db import models

from method.models import MethodWorkbookBase


class WorklistColumn(models.Model):

    name = models.CharField(max_length=255)
    method = models.ForeignKey(to=MethodWorkbookBase, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.method}|{self.name}"


class WorklistColumnValue(models.Model):
    worklist_column = models.ForeignKey(to=WorklistColumn, on_delete=models.CASCADE)
    row = models.IntegerField()
    value = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.worklist_column}:{self.row} -> {self.value}"
