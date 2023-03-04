from __future__ import annotations
import dataclasses
import requests
from ..shared import deletemodelresponse as shared_deletemodelresponse
from typing import Optional


@dataclasses.dataclass
class DeleteModelPathParams:
    model: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteModelRequest:
    path_params: DeleteModelPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_model_response: Optional[shared_deletemodelresponse.DeleteModelResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    