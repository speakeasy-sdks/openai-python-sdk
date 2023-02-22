import dataclasses
from ..shared import deletefileresponse as shared_deletefileresponse
from typing import Optional


@dataclasses.dataclass
class DeleteFilePathParams:
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteFileRequest:
    path_params: DeleteFilePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_file_response: Optional[shared_deletefileresponse.DeleteFileResponse] = dataclasses.field(default=None)
    