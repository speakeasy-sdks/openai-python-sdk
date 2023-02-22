import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class CreateImageEditRequestImage:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    image: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'image' }})
    

@dataclasses.dataclass
class CreateImageEditRequestMask:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    mask: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'mask' }})
    

@dataclasses.dataclass
class CreateImageEditRequest:
    image: CreateImageEditRequestImage = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    prompt: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'prompt' }})
    mask: Optional[CreateImageEditRequestMask] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    n: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'n' }})
    response_format: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'response_format' }})
    size: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'size' }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'user' }})
    