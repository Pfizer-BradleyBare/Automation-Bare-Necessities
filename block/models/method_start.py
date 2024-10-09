from excel.definitions import BlockDefinitionExcelDefinition

from .block_base import BlockBase


class MethodStart(BlockBase):

    def validate(self):
        """No validation to perform for this step. It is just a starting step."""
        return

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        return BlockDefinitionExcelDefinition(
            name="--Method Start--",
            category="__IGNORE__",
            hexidecimal_color="2CAE66",
            text_hexidecimal_color="000000",
        )
