from __future__ import annotations

from typing import Any, cast

import xlwings

from method.models.user_method import UserMethodWorkbookBase
from worklist.models import WorklistColumn, WorklistColumnValue


def read_worklist(method: UserMethodWorkbookBase, sheet: xlwings.Sheet):

    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    for column_index in range(len(rows[0])):
        column = [row[column_index] for row in rows]

        column_name = column[0]

        if column_name is None:
            continue

        worklist_column = WorklistColumn(name=column_name, method=method)
        worklist_column.clean()
        worklist_column.save()

        column_values = column[1:]

        for row, value in enumerate(column_values):
            worklist_column_value = WorklistColumnValue(
                worklist_column=worklist_column,
                row=row,
                value=value,
            )
            worklist_column_value.clean()
            worklist_column_value.save()
