"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import finetune as shared_finetune
from typing import Optional



@dataclasses.dataclass
class RetrieveFineTuneRequest:
    fine_tune_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tune_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the fine-tune job"""
    




@dataclasses.dataclass
class RetrieveFineTuneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fine_tune: Optional[shared_finetune.FineTune] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

