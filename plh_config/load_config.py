from collections import defaultdict

from plh import implementation

from plh_config.backend.models import BackendBase
from plh_config.carrier.models import CarrierBase
from plh_config.carrier_loader.models import CarrierLoaderBase
from plh_config.centrifuge.models import CentrifugeBase
from plh_config.closeable_container.models import CloseableContainerBase
from plh_config.deck_location.models import DeckLocationBase
from plh_config.heat_cool_shake.models import HeatCoolShakeBase
from plh_config.labware.models import LabwareBase
from plh_config.layout_item.models import LayoutItemBase
from plh_config.pipette.models import PipetteBase
from plh_config.storage_device.models import StorageDeviceBase
from plh_config.tip.models import TipBase
from plh_config.transport.models import TransportBase


def load_config():

    # backend

    json = defaultdict(list)
    for item in BackendBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.backend.load(json)

    # carrier

    json = defaultdict(list)
    for item in CarrierBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.carrier.load(json)

    # carrier loader

    json = defaultdict(list)
    for item in CarrierLoaderBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.carrier_loader.load(json)

    # labware

    json = defaultdict(list)
    for item in LabwareBase.objects.all():
        additional_config = {}

        layout_type = item.labware_definition_type
        layout_direction = item.labware_definition_direction
        layout_rows = item.labware_defintion_rows
        layout_cols = item.labware_defintion_columns

        additional_config["layout"] = {
            "type": layout_type,
            "direction": layout_direction,
            "columns": layout_cols,
            "rows": layout_rows,
        }

        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.labware.load(json)

    # transport

    json = defaultdict(list)
    for item in TransportBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.transport.load(json)

    # deck location

    json = defaultdict(list)
    for item in DeckLocationBase.objects.all():
        additional_config = {}

        additional_config["carrier"] = str(item.carrier)

        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.deck_location.load(json)

    # layout item

    json = defaultdict(list)
    for item in LayoutItemBase.objects.all():
        additional_config = {}

        additional_config["deck_location"] = str(item.deck_location)
        additional_config["labware"] = str(item.labware)

        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.layout_item.load(json)

    # tip

    json = defaultdict(list)
    for item in TipBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.tip.load(json)

    # closeable container

    json = defaultdict(list)
    for item in CloseableContainerBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.closeable_container.load(json)

    # heat cool shake

    json = defaultdict(list)
    for item in HeatCoolShakeBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.heat_cool_shake.load(json)

    # pipette

    json = defaultdict(list)
    for item in PipetteBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.pipette.load(json)

    # storage device

    json = defaultdict(list)
    for item in StorageDeviceBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.storage_device.load(json)

    # centrifuge

    json = defaultdict(list)
    for item in CentrifugeBase.objects.all():
        additional_config = {}
        json[type(item).__name__].append(vars(item) | additional_config)
    implementation.centrifuge.load(json)
