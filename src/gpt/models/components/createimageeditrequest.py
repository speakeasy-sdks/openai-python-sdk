"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional, Union


@dataclasses.dataclass
class CreateImageEditRequestImage:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'image' }})
    



@dataclasses.dataclass
class Mask:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'mask' }})
    


class CreateImageEditRequest2(str, Enum):
    r"""The model to use for image generation. Only `dall-e-2` is supported at this time."""
    DALL_E_2 = 'dall-e-2'

class CreateImageEditRequestResponseFormat(str, Enum):
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    URL = 'url'
    B64_JSON = 'b64_json'

class Size(str, Enum):
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`."""
    TWO_HUNDRED_AND_FIFTY_SIXX256 = '256x256'
    FIVE_HUNDRED_AND_TWELVEX512 = '512x512'
    ONE_THOUSAND_AND_TWENTY_FOURX1024 = '1024x1024'


@dataclasses.dataclass
class CreateImageEditRequest:
    image: CreateImageEditRequestImage = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    r"""The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask."""
    prompt: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'prompt' }})
    r"""A text description of the desired image(s). The maximum length is 1000 characters."""
    mask: Optional[Mask] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    r"""An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`."""
    model: Optional[Union[str, CreateImageEditRequest2]] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'model' }})
    r"""The model to use for image generation. Only `dall-e-2` is supported at this time."""
    n: Optional[int] = dataclasses.field(default=1, metadata={'multipart_form': { 'field_name': 'n' }})
    r"""The number of images to generate. Must be between 1 and 10."""
    response_format: Optional[CreateImageEditRequestResponseFormat] = dataclasses.field(default=CreateImageEditRequestResponseFormat.URL, metadata={'multipart_form': { 'field_name': 'response_format' }})
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    size: Optional[Size] = dataclasses.field(default=Size.ONE_THOUSAND_AND_TWENTY_FOURX1024, metadata={'multipart_form': { 'field_name': 'size' }})
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'user' }})
    r"""A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)."""
    

