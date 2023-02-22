import dataclasses
from ..shared import createcompletionrequest as shared_createcompletionrequest
from ..shared import createcompletionresponse as shared_createcompletionresponse
from typing import Optional


@dataclasses.dataclass
class CreateCompletionRequest:
    request: shared_createcompletionrequest.CreateCompletionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateCompletionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_completion_response: Optional[shared_createcompletionresponse.CreateCompletionResponse] = dataclasses.field(default=None)
    