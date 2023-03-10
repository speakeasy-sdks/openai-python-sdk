from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createimagevariationrequest as shared_createimagevariationrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateImageVariationRequest:
    request: shared_createimagevariationrequest.CreateImageVariationRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateImageVariationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    images_response: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    