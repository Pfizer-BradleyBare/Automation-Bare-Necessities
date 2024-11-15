from django.db import models as _dm
from polymorphic import models as _dpm

from . import metaclasses as _mc


class AbstractModel(_dm.Model, metaclass=_mc._AbstractModelMeta):
    # You may have common fields here.

    class Meta:
        abstract = True


class AbstractPolymorphicModel(
    _dpm.PolymorphicModel,
    metaclass=_mc._AbstractPolymorphicModelMeta,
):
    # You may have common fields here.

    class Meta:
        abstract = True
