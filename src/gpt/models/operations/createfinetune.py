from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createfinetunerequest as shared_createfinetunerequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateFineTuneRequest:
    request: shared_createfinetunerequest.CreateFineTuneRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateFineTuneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fine_tune: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    