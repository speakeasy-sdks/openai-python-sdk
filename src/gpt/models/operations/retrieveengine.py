from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveEngineRequest:
    engine_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'engine_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveEngineResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    engine: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    