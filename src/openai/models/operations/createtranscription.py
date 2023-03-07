from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createtranscriptionrequest as shared_createtranscriptionrequest
from ..shared import createtranscriptionresponse as shared_createtranscriptionresponse
from typing import Optional


@dataclasses.dataclass
class CreateTranscriptionRequest:
    request: shared_createtranscriptionrequest.CreateTranscriptionRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateTranscriptionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_transcription_response: Optional[shared_createtranscriptionresponse.CreateTranscriptionResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    