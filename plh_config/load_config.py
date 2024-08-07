from collections import defaultdict

from plh import implementation

from plh_config.backend.models import BackendBase
from plh_config.carrier.models import CarrierBase


def load_config():

    json = {}
    for item in BackendBase.objects.all():
        json[type(item).__name__] = vars(item)

    implementation.backend.load(json)

    json = defaultdict(list)
    for item in CarrierBase.objects.all():
        json[type(item).__name__].append(vars(item))

    implementation.carrier.load(json)

    print(implementation.backend.devices)
    print(implementation.carrier.devices)
