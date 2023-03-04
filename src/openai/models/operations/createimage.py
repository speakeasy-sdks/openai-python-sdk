from __future__ import annotations
import dataclasses
import requests
from ..shared import createimagerequest as shared_createimagerequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateImageRequest:
    request: shared_createimagerequest.CreateImageRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateImageResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    images_response: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    