from __future__ import annotations
import dataclasses
from ..shared import listmodelsresponse as shared_listmodelsresponse
from typing import Optional


@dataclasses.dataclass
class ListModelsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_models_response: Optional[shared_listmodelsresponse.ListModelsResponse] = dataclasses.field(default=None)
    