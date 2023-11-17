"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import deletethreadresponse as components_deletethreadresponse
from typing import Optional


@dataclasses.dataclass
class DeleteThreadRequest:
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the thread to delete."""
    



@dataclasses.dataclass
class DeleteThreadResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_thread_response: Optional[components_deletethreadresponse.DeleteThreadResponse] = dataclasses.field(default=None)
    r"""OK"""
    
