from .container_base import ContainerBase


class Biorad200uLWell(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 200

    @classmethod
    def dead_volume(cls) -> float:
        return 10

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(242.1231, 14.68)]
