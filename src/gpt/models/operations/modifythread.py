"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import modifythreadrequest as components_modifythreadrequest
from ...models.components import threadobject as components_threadobject
from typing import Optional


@dataclasses.dataclass
class ModifyThreadRequest:
    modify_thread_request: components_modifythreadrequest.ModifyThreadRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the thread to modify. Only the `metadata` can be modified."""
    



@dataclasses.dataclass
class ModifyThreadResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    thread_object: Optional[components_threadobject.ThreadObject] = dataclasses.field(default=None)
    r"""OK"""
    

