from __future__ import annotations
import dataclasses
from ..shared import createfilerequest as shared_createfilerequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateFileRequest:
    request: shared_createfilerequest.CreateFileRequest = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    open_ai_file: Optional[Any] = dataclasses.field(default=None)
    