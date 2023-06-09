"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
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
    r"""The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask."""
    prompt: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'prompt' }})
    r"""A text description of the desired image(s). The maximum length is 1000 characters."""
    mask: Optional[CreateImageEditRequestMask] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    r"""An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`."""
    n: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'n' }})
    response_format: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'response_format' }})
    size: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'size' }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'user' }})
    