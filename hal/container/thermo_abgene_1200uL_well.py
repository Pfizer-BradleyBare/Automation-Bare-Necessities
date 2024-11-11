from .container_base import ContainerBase


class ThermoAbgene1200uLWell(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 1200

    @classmethod
    def dead_volume(cls) -> float:
        return 10

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(83.1264, 3), (1353.2064, 21)]
