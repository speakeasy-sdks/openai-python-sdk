from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveModelRequest:
    model: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    