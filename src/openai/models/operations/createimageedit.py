from __future__ import annotations
import dataclasses
import requests
from ..shared import createimageeditrequest as shared_createimageeditrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateImageEditRequest:
    request: shared_createimageeditrequest.CreateImageEditRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateImageEditResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    images_response: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    