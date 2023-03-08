from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createsearchrequest as shared_createsearchrequest
from ..shared import createsearchresponse as shared_createsearchresponse
from typing import Optional


@dataclasses.dataclass
class CreateSearchPathParams:
    engine_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'engine_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateSearchRequest:
    path_params: CreateSearchPathParams = dataclasses.field()
    request: shared_createsearchrequest.CreateSearchRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_search_response: Optional[shared_createsearchresponse.CreateSearchResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    