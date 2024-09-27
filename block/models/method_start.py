from excel.definitions import BlockDefinitionExcelDefinition

from .block_base import BlockBase


class MethodStart(BlockBase):

    def get_excel_definition(self) -> BlockDefinitionExcelDefinition:
        return BlockDefinitionExcelDefinition(
            name="--Method Start--",
            category="__IGNORE__",
            hexidecimal_color="66cf22",
        )
