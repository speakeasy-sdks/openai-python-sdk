from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listfinetunesresponse as shared_listfinetunesresponse
from typing import Optional


@dataclasses.dataclass
class ListFineTunesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_fine_tunes_response: Optional[shared_listfinetunesresponse.ListFineTunesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    