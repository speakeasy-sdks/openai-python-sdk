from __future__ import annotations
import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveModelPathParams:
    model: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveModelRequest:
    path_params: RetrieveModelPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model: Optional[Any] = dataclasses.field(default=None)
    