from __future__ import annotations
import dataclasses
from ..shared import createanswerrequest as shared_createanswerrequest
from ..shared import createanswerresponse as shared_createanswerresponse
from typing import Optional


@dataclasses.dataclass
class CreateAnswerRequest:
    request: shared_createanswerrequest.CreateAnswerRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateAnswerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_answer_response: Optional[shared_createanswerresponse.CreateAnswerResponse] = dataclasses.field(default=None)
    