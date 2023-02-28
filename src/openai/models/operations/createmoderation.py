from __future__ import annotations
import dataclasses
from ..shared import createmoderationrequest as shared_createmoderationrequest
from ..shared import createmoderationresponse as shared_createmoderationresponse
from typing import Optional


@dataclasses.dataclass
class CreateModerationRequest:
    request: shared_createmoderationrequest.CreateModerationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateModerationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_moderation_response: Optional[shared_createmoderationresponse.CreateModerationResponse] = dataclasses.field(default=None)
    