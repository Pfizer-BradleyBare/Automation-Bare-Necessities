from .container_base import ContainerBase


class UnchainedLabsUVReaderWell(ContainerBase):
    @classmethod
    def simultaneous_tips(cls) -> int:
        return 1

    @classmethod
    def max_volume(cls) -> float:
        return 3

    @classmethod
    def dead_volume(cls) -> float:
        return 0

    @classmethod
    def shape_definition(cls) -> list[tuple[float, float]]:
        return [
            (9.42e-05, 0.001),
            (0.0340182, 0.121),
            (0.0772432, 0.251),
            (1.9683132, 1.201),
            (5.0696632, 1.901),
        ]
