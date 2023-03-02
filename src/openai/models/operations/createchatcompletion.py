from __future__ import annotations
import dataclasses
from ..shared import createchatcompletionrequest as shared_createchatcompletionrequest
from ..shared import createchatcompletionresponse as shared_createchatcompletionresponse
from typing import Optional


@dataclasses.dataclass
class CreateChatCompletionRequest:
    request: shared_createchatcompletionrequest.CreateChatCompletionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateChatCompletionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_chat_completion_response: Optional[shared_createchatcompletionresponse.CreateChatCompletionResponse] = dataclasses.field(default=None)
    