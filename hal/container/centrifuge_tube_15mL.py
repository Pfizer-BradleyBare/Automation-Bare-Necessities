from .container_base import ContainerBase


class CentrifugeTube15mL(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 15000

    @classmethod
    def dead_volume(cls) -> float:
        return 500

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(1461.004, 23.36), (15269.62, 118.61)]
