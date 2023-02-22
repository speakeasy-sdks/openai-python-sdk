import dataclasses
from ..shared import listfilesresponse as shared_listfilesresponse
from typing import Optional


@dataclasses.dataclass
class ListFilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_files_response: Optional[shared_listfilesresponse.ListFilesResponse] = dataclasses.field(default=None)
    