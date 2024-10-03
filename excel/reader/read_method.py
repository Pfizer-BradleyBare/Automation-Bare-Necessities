import xlwings

from method.models import UserMethodWorkbookBase


def read_method(method: UserMethodWorkbookBase, sheet: xlwings.Sheet): ...
