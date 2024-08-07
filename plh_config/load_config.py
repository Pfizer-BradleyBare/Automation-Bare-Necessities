from plh import implementation

from plh_config.backend.models import BackendBase


def load_config():

    implementation.backend.load(
        {type(b).__name__: vars(b) for b in BackendBase.objects.all()},
    )
