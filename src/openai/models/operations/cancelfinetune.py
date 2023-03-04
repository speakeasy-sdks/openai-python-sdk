from __future__ import annotations
import dataclasses
import requests
from typing import Any, Optional


@dataclasses.dataclass
class CancelFineTunePathParams:
    fine_tune_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tune_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CancelFineTuneRequest:
    path_params: CancelFineTunePathParams = dataclasses.field()
    

@dataclasses.dataclass
class CancelFineTuneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fine_tune: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    