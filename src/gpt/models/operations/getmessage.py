"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import messageobject as components_messageobject
from typing import Optional


@dataclasses.dataclass
class GetMessageRequest:
    message_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'message_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the message to retrieve."""
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the [thread](/docs/api-reference/threads) to which this message belongs."""
    



@dataclasses.dataclass
class GetMessageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    message_object: Optional[components_messageobject.MessageObject] = dataclasses.field(default=None)
    r"""OK"""
    

