from typing import Any, cast

import xlwings
from loguru import logger

from block.models import BlockBase, MethodStart
from method.models import MethodWorkbookBase


def read_block(
    method: MethodWorkbookBase,
    sheet: xlwings.Sheet,
    row_index: int,
    column_index: int,
) -> BlockBase:
    bound_logger = logger.bind(
        source="ABN",
        method=str(method),
        row_index=row_index,
        column_index=column_index,
    )

    bound_logger.debug("read_block")

    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    query = BlockBase.objects.filter(
        method=method,
        row=row_index,
        column=column_index,
    )

    if query.exists():
        bound_logger.debug("Block already read")
        return query.get()

    block_type_name = (
        cast(str, rows[row_index][column_index])
        .replace(
            " (click here to update)",
            "",
        )
        .replace(" ", "")
    )

    bound_logger.debug(f"Reading '{block_type_name}")

    # extract parameters
    parameters: dict[str, Any] = {}

    parameters["method"] = method
    parameters["row"] = row_index
    parameters["column"] = column_index

    bound_logger.debug("Reading parameters")

    while True:
        row_index += 1

        label = cast(str, rows[row_index][column_index])
        value = rows[row_index][column_index + 1]

        if label == "Advanced Options":
            continue

        if label is None:
            break

        parameters[label] = value

    block = BlockBase.block_subclasses[block_type_name]()
    block.assign_parameters(**parameters)
    block.validate_parameters()

    bound_logger.debug("Block read")

    return block


def read_recursive(
    method: MethodWorkbookBase,
    sheet: xlwings.Sheet,
    row_index: int,
    column_index: int,
):
    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    parent_block = cast(
        BlockBase,
        BlockBase.objects.filter(
            method=method,
            row=row_index,
            column=column_index,
        ).get(),
    )

    while True:
        # Find first empty cell
        while rows[row_index][column_index] is not None:
            row_index += 1

        # Is it possible that there is another middle step coming?
        if rows[row_index + 1][column_index + 1] == "Add Action (click here)":
            # Attempt to find a middle block.
            # It's possible there is not one, in which case we catch the index error and end.
            try:
                while rows[row_index][column_index] is None:
                    row_index += 1

            except IndexError:
                # We reached the end of the used range.
                return

            block = read_block(
                method=method,
                sheet=sheet,
                row_index=row_index,
                column_index=column_index,
            )

            block.middle_parent = parent_block
            parent_block.middle_child = block

            block.clean()
            block.save()
            parent_block.clean()
            parent_block.save()

        # Nope we are at a Merge or SplitWorklist step
        else:
            # Since this is a Merge or Split Worklist, we are guarenteed to find 1 or 2 Activate Container blocks

            column_counter = 2

            while True:
                try:
                    left_cell_value = rows[row_index + 1][column_index - column_counter]
                except IndexError:
                    left_cell_value = ""

                try:
                    right_cell_value = rows[row_index + 1][
                        column_index + column_counter
                    ]
                except IndexError:
                    right_cell_value = ""

                if (
                    left_cell_value == "Activate Container"
                    or right_cell_value == "Activate Container"
                ):
                    break

                column_counter += 2

            if left_cell_value == "Activate Container":
                block = read_block(
                    method=method,
                    sheet=sheet,
                    row_index=row_index + 1,
                    column_index=column_index - column_counter,
                )

                block.right_parent = parent_block
                parent_block.left_child = block

                block.clean()
                block.save()
                parent_block.clean()
                parent_block.save()

                read_recursive(
                    method=method,
                    sheet=sheet,
                    row_index=row_index + 1,
                    column_index=column_index - column_counter,
                )

            if right_cell_value == "Activate Container":
                block = read_block(
                    method=method,
                    sheet=sheet,
                    row_index=row_index + 1,
                    column_index=column_index + column_counter,
                )

                block.left_parent = parent_block
                parent_block.right_child = block

                block.clean()
                block.save()
                parent_block.clean()
                parent_block.save()

                read_recursive(
                    method=method,
                    sheet=sheet,
                    row_index=row_index + 1,
                    column_index=column_index + column_counter,
                )

            return

        parent_block = block


def read_method(method: MethodWorkbookBase, sheet: xlwings.Sheet):
    bound_logger = logger.bind(
        source="ABN",
        method=str(method),
    )

    bound_logger.debug("read_method")

    row_index = 0
    column_index = 0

    rows: list[list[Any]] = cast(list, sheet.used_range.value)

    while True:
        row = rows[row_index]

        if "--Method Start--" in row:
            column_index = row.index("--Method Start--")
            break

        row_index += 1

    bound_logger.debug(f"Method start found at row={row_index}, column={column_index}")

    start_step = MethodStart(method=method, row=row_index, column=column_index)
    # Normalize with Excel rows and columns (1 indexed)
    start_step.clean()
    start_step.save()

    read_recursive(
        method=method,
        sheet=sheet,
        row_index=row_index,
        column_index=column_index,
    )
