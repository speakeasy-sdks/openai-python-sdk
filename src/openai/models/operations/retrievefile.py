import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class RetrieveFilePathParams:
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveFileRequest:
    path_params: RetrieveFilePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    open_ai_file: Optional[Any] = dataclasses.field(default=None)
    