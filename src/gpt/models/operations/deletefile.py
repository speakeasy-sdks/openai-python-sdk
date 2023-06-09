"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deletefileresponse as shared_deletefileresponse
from typing import Optional


@dataclasses.dataclass
class DeleteFileRequest:
    
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the file to use for this request"""
    

@dataclasses.dataclass
class DeleteFileResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_file_response: Optional[shared_deletefileresponse.DeleteFileResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    