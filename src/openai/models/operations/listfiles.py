from __future__ import annotations
import dataclasses
import requests
from ..shared import listfilesresponse as shared_listfilesresponse
from typing import Optional


@dataclasses.dataclass
class ListFilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_files_response: Optional[shared_listfilesresponse.ListFilesResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    