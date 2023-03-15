from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createclassificationresponse as shared_createclassificationresponse
from typing import Optional


@dataclasses.dataclass
class CreateClassificationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_classification_response: Optional[shared_createclassificationresponse.CreateClassificationResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    