from django.db import models

from excel.definitions import BlockDefinitionExcelDefinition

from ..block_base import BlockBase


class RuntimeComment(BlockBase):

    comment_text = models.TextField()
    wait_for_user_confirmation = models.CharField(max_length=100, blank=True)

    @classmethod
    def get_excel_definition(cls) -> BlockDefinitionExcelDefinition:
        definition = BlockDefinitionExcelDefinition(
            name="Runtime Comment",
            category="Comments",
            hexidecimal_color="F7EF70",
            text_hexidecimal_color="000000",
        )

        definition.add_parameter(
            label="Comment Text",
            advanced=False,
            default_value="",
            dropdown_items="",
            free_text=True,
        )

        definition.add_parameter(
            label="Wait For User Confirmation",
            advanced=True,
            default_value="Yes",
            dropdown_items="Yes",
            free_text=False,
        )

        return definition

    def assign_parameters(self, parameters: dict):
        self.comment_text = parameters["Comment Text"]
        
        try:
            self.wait_for_user_confirmation = parameters["Wait For User Confirmation"]
        except KeyError:
            self.wait_for_user_confirmation = ""
        
        return super().assign_parameters(parameters)