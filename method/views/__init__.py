from .templates_index import TemplatesIndexView
from .test_index import TestIndexView
from .test_preparation_list import TestPreparationListView
from .test_progress import TestProgressView
from .test_progress_body import TestProgressBodyView

__all__ = [
    "TestIndexView",
    "TestProgressView",
    "TestProgressBodyView",
    "TestPreparationListView",
    "TemplatesIndexView",
]
