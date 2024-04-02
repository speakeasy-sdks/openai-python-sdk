"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import openaifile as components_openaifile
from typing import Optional


@dataclasses.dataclass
class RetrieveFileRequest:
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the file to use for this request."""
    



@dataclasses.dataclass
class RetrieveFileResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    open_ai_file: Optional[components_openaifile.OpenAIFile] = dataclasses.field(default=None)
    r"""OK"""
    

