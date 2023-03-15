from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class CreateFineTuneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fine_tune: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    