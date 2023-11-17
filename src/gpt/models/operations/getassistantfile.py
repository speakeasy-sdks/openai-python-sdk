"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import assistantfileobject as components_assistantfileobject
from typing import Optional


@dataclasses.dataclass
class GetAssistantFileRequest:
    assistant_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'assistant_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the assistant who the file belongs to."""
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the file we're getting."""
    



@dataclasses.dataclass
class GetAssistantFileResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    assistant_file_object: Optional[components_assistantfileobject.AssistantFileObject] = dataclasses.field(default=None)
    r"""OK"""
    
