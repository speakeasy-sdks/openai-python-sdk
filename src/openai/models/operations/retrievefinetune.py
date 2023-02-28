from __future__ import annotations
import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveFineTunePathParams:
    fine_tune_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tune_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveFineTuneRequest:
    path_params: RetrieveFineTunePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveFineTuneResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fine_tune: Optional[Any] = dataclasses.field(default=None)
    