from __future__ import annotations

from ..definition import BlockDefinition
from .block_base import BlockBase


class MethodStart(BlockBase):
    @classmethod
    def get_definition(cls) -> BlockDefinition:
        return BlockDefinition(
            name="--Method Start--",
            category="__IGNORE__",
            hexidecimal_color="2CAE66",
            text_hexidecimal_color="000000",
        )
