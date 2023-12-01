"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import model as components_model
from typing import Optional


@dataclasses.dataclass
class RetrieveModelRequest:
    model: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model', 'style': 'simple', 'explode': False }})
    r"""The ID of the model to use for this request"""
    



@dataclasses.dataclass
class RetrieveModelResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    model: Optional[components_model.Model] = dataclasses.field(default=None)
    r"""OK"""
    

