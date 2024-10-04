from typing import Any, cast

import xlwings

from method.models import UserMethodWorkbookBase


def read_recursive(
    method: UserMethodWorkbookBase,
    sheet: xlwings.Sheet,
    row_index: int,
    column_index: int,
): ...


def read_method(method: UserMethodWorkbookBase, sheet: xlwings.Sheet):

    row_index = 0
    column_index = 0

    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    while True:
        row = rows[row_index]

        if "--Method Start--" in row:
            column_index = row.index("--Method Start--")
            break

        row_index += 1

    print(row_index)
    print(column_index)
