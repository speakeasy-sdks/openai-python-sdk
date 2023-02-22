import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveEnginePathParams:
    engine_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'engine_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveEngineRequest:
    path_params: RetrieveEnginePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveEngineResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    engine: Optional[Any] = dataclasses.field(default=None)
    