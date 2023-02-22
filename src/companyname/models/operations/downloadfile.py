import dataclasses
from typing import Optional


@dataclasses.dataclass
class DownloadFilePathParams:
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadFileRequest:
    path_params: DownloadFilePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DownloadFileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    download_file_200_application_json_string: Optional[str] = dataclasses.field(default=None)
    