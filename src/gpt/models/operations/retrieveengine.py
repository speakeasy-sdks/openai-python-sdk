"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import engine as shared_engine
from typing import Optional


@dataclasses.dataclass
class RetrieveEngineRequest:
    
    engine_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'engine_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the engine to use for this request"""  
    

@dataclasses.dataclass
class RetrieveEngineResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    engine: Optional[shared_engine.Engine] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    