import pythoncom
import xlwings
from loguru import logger

from block.models import BlockBase
from method.models import MethodWorkbookBase

from .read_method import read_method
from .read_solutions import read_solutions
from .read_worklist import read_worklist


def read_workbook(method: MethodWorkbookBase):
    bound_logger = logger.bind(
        source="ABN",
        method=str(method),
    )

    bound_logger.debug("read_workbook")

    pythoncom.CoInitialize()

    with xlwings.App(visible=False, add_book=False) as app, app.books.open(
        method.file.path,
    ) as book:
        bound_logger.debug("Workbook opened")

        try:
            book.app.macro("abn_v3_workbook")()
            bound_logger.debug("Workbook confirmed to be ABN v3.0 compatible")

        except pythoncom.com_error:
            bound_logger.exception("Workbook is NOT ABN v3.0 compatible. Aborting")
            method.delete()
            return

        read_solutions(method, book.sheets["Solutions"])
        read_worklist(method, book.sheets["Worklist"])
        read_method(method, book.sheets["Method"])

        method.is_full_read = True
        method.clean()
        method.save()

        bound_logger.info("Workbook read")

        if BlockBase.objects.filter(method=method, is_valid=False).exists():
            bound_logger.critical(f"Method '{method}' failed validation")
            method.delete()
