from __future__ import annotations
import dataclasses
from ..shared import listenginesresponse as shared_listenginesresponse
from typing import Optional


@dataclasses.dataclass
class ListEnginesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_engines_response: Optional[shared_listenginesresponse.ListEnginesResponse] = dataclasses.field(default=None)
    