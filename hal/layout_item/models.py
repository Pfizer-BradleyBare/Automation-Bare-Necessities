from django.db import models


# Create your models here.
class LayoutItemBase: ...


class Lid(LayoutItemBase): ...


class TipRack(LayoutItemBase): ...


class VacuumManifold(LayoutItemBase): ...


class Plate(LayoutItemBase): ...


class FilterPlate(Plate): ...


class CoverablePlate(Plate):
    lid = models.ForeignKey(
        to="Lid",
        on_delete=models.CASCADE,
        name="lid_id",
        db_column="lid_id",
    )


class CoverableFilterPlate(CoverablePlate): ...
