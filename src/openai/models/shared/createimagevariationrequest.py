from __future__ import annotations
import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class CreateImageVariationRequestImage:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    image: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'image' }})
    

@dataclasses.dataclass
class CreateImageVariationRequest:
    image: CreateImageVariationRequestImage = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    n: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'n' }})
    response_format: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'response_format' }})
    size: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'size' }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'user' }})
    