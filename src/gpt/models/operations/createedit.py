from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createeditresponse as shared_createeditresponse
from typing import Optional


@dataclasses.dataclass
class CreateEditResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_edit_response: Optional[shared_createeditresponse.CreateEditResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    