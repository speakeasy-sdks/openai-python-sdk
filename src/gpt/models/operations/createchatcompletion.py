from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createchatcompletionresponse as shared_createchatcompletionresponse
from typing import Optional


@dataclasses.dataclass
class CreateChatCompletionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_chat_completion_response: Optional[shared_createchatcompletionresponse.CreateChatCompletionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    