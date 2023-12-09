"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import threadobject as components_threadobject
from typing import Optional


@dataclasses.dataclass
class GetThreadRequest:
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the thread to retrieve."""
    



@dataclasses.dataclass
class GetThreadResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    thread_object: Optional[components_threadobject.ThreadObject] = dataclasses.field(default=None)
    r"""OK"""
    

