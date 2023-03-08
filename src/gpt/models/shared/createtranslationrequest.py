from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class CreateTranslationRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclasses.dataclass
class CreateTranslationRequest:
    file: CreateTranslationRequestFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    model: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'model' }})
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'prompt' }})
    response_format: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'response_format' }})
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'temperature' }})
    