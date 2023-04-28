"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createsearchrequest as shared_createsearchrequest
from ..shared import createsearchresponse as shared_createsearchresponse
from typing import Optional


@dataclasses.dataclass
class CreateSearchRequest:
    
    create_search_request: shared_createsearchrequest.CreateSearchRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})

    engine_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'engine_id', 'style': 'simple', 'explode': False }})

    r"""The ID of the engine to use for this request.  You can select one of `ada`, `babbage`, `curie`, or `davinci`."""
    

@dataclasses.dataclass
class CreateSearchResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    create_search_response: Optional[shared_createsearchresponse.CreateSearchResponse] = dataclasses.field(default=None)

    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    