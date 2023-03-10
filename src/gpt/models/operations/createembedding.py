from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createembeddingrequest as shared_createembeddingrequest
from ..shared import createembeddingresponse as shared_createembeddingresponse
from typing import Optional


@dataclasses.dataclass
class CreateEmbeddingRequest:
    request: shared_createembeddingrequest.CreateEmbeddingRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateEmbeddingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_embedding_response: Optional[shared_createembeddingresponse.CreateEmbeddingResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    