from __future__ import annotations
import dataclasses
from ..shared import createeditrequest as shared_createeditrequest
from ..shared import createeditresponse as shared_createeditresponse
from typing import Optional


@dataclasses.dataclass
class CreateEditRequest:
    request: shared_createeditrequest.CreateEditRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateEditResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_edit_response: Optional[shared_createeditresponse.CreateEditResponse] = dataclasses.field(default=None)
    