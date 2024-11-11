from .container_base import ContainerBase


class ReagentReservoir60mL(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 60000

    @classmethod
    def dead_volume(cls) -> float:
        return 500

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(3603.027, 6.72), (80009.43, 62.72)]
