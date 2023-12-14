"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union

class CreateImageRequest2(str, Enum):
    r"""The model to use for image generation."""
    DALL_E_2 = 'dall-e-2'
    DALL_E_3 = 'dall-e-3'

class Quality(str, Enum):
    r"""The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`."""
    STANDARD = 'standard'
    HD = 'hd'

class CreateImageRequestResponseFormat(str, Enum):
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    URL = 'url'
    B64_JSON = 'b64_json'

class CreateImageRequestSize(str, Enum):
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models."""
    TWO_HUNDRED_AND_FIFTY_SIXX256 = '256x256'
    FIVE_HUNDRED_AND_TWELVEX512 = '512x512'
    ONE_THOUSAND_AND_TWENTY_FOURX1024 = '1024x1024'
    ONE_THOUSAND_SEVEN_HUNDRED_AND_NINETY_TWOX1024 = '1792x1024'
    ONE_THOUSAND_AND_TWENTY_FOURX1792 = '1024x1792'

class Style(str, Enum):
    r"""The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`."""
    VIVID = 'vivid'
    NATURAL = 'natural'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateImageRequest:
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})
    r"""A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`."""
    model: Optional[Union[str, CreateImageRequest2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The model to use for image generation."""
    n: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n') }})
    r"""The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported."""
    quality: Optional[Quality] = dataclasses.field(default=Quality.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quality'), 'exclude': lambda f: f is None }})
    r"""The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`."""
    response_format: Optional[CreateImageRequestResponseFormat] = dataclasses.field(default=CreateImageRequestResponseFormat.URL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response_format') }})
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    size: Optional[CreateImageRequestSize] = dataclasses.field(default=CreateImageRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size') }})
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models."""
    style: Optional[Style] = dataclasses.field(default=Style.VIVID, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('style') }})
    r"""The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)."""
    

