from .container_base import ContainerBase


class CorningCostar2000uLVBottomWell(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 2000

    @classmethod
    def dead_volume(cls) -> float:
        return 10

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [(134.0416, 4), (2566.0416, 42)]
