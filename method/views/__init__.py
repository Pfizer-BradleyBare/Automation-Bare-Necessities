from .templates_blank import TemplatesBlankView
from .templates_index import TemplatesIndexView
from .templates_method import TemplatesMethodView
from .templates_update import TemplatesUpdateView
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
    "TemplatesBlankView",
    "TemplatesMethodView",
    "TemplatesUpdateView",
]
