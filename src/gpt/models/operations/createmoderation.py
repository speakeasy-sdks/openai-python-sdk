from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createmoderationresponse as shared_createmoderationresponse
from typing import Optional


@dataclasses.dataclass
class CreateModerationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_moderation_response: Optional[shared_createmoderationresponse.CreateModerationResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    