import pythoncom
import xlwings
from loguru import logger

from method.models import (
    MethodWorkbookBase,
)

from .read_method import read_method
from .read_solutions import read_solutions
from .read_worklist import read_worklist


def read_workbook(method: MethodWorkbookBase):
    bound_logger = logger.bind(
        source="ABN",
        method=str(method),
    )

    bound_logger.info("Starting read of method workbook")

    pythoncom.CoInitialize()

    with xlwings.App(visible=False, add_book=False) as app, app.books.open(
        method.file.path,
    ) as book:
        bound_logger.debug("Workbook opened")

        try:
            book.app.macro("abn_v3_workbook")()
            bound_logger.info("Workbook confirmed to be ABN v3.0 compatible")

        except pythoncom.com_error:
            bound_logger.exception("Workbook is NOT ABN v3.0 compatible. Aborting")
            method.delete()
            return

        read_solutions(method, book.sheets["Solutions"])
        method.solutions_read_checkpoint = True
        method.clean()
        method.save()

        read_worklist(method, book.sheets["Worklist"])
        method.worklist_read_checkpoint = True
        method.clean()
        method.save()

        read_method(method, book.sheets["Method"])
        method.method_read_checkpoint = True
        method.clean()
        method.save()

    bound_logger.debug("Workbook closed")

    bound_logger.info("Completed read of method workbook")
