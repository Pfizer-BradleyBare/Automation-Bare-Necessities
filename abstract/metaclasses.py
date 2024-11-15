from abc import ABCMeta

from django.db import models as _dm
from polymorphic import models as _dpm


class _AbstractModelMeta(ABCMeta, type(_dm.Model)):  # type:ignore
    pass


class _AbstractPolymorphicModelMeta(ABCMeta, type(_dpm.PolymorphicModel)):  # type:ignore
    pass
