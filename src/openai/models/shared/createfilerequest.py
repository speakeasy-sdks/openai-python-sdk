from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class CreateFileRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclasses.dataclass
class CreateFileRequest:
    file: CreateFileRequestFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    purpose: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'purpose' }})
    