from .container_base import ContainerBase


class Thermo400uLWell(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 400

    @classmethod
    def dead_volume(cls) -> float:
        return 10

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(56.745, 3), (510.705, 11)]
