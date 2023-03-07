from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createtranslationrequest as shared_createtranslationrequest
from ..shared import createtranslationresponse as shared_createtranslationresponse
from typing import Optional


@dataclasses.dataclass
class CreateTranslationRequest:
    request: shared_createtranslationrequest.CreateTranslationRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateTranslationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_translation_response: Optional[shared_createtranslationresponse.CreateTranslationResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    