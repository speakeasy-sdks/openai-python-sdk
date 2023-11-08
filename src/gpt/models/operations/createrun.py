"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import createrunrequest as components_createrunrequest
from ...models.components import runobject as components_runobject
from typing import Optional


@dataclasses.dataclass
class CreateRunRequest:
    create_run_request: components_createrunrequest.CreateRunRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the thread to run."""
    



@dataclasses.dataclass
class CreateRunResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    run_object: Optional[components_runobject.RunObject] = dataclasses.field(default=None)
    r"""OK"""
    

