"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional

class CreateImageRequestResponseFormat(str, Enum):
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    URL = 'url'
    B64_JSON = 'b64_json'

class CreateImageRequestSize(str, Enum):
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`."""
    TWO_HUNDRED_AND_FIFTY_SIXX256 = '256x256'
    FIVE_HUNDRED_AND_TWELVEX512 = '512x512'
    ONE_THOUSAND_AND_TWENTY_FOURX1024 = '1024x1024'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateImageRequest:
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})
    r"""A text description of the desired image(s). The maximum length is 1000 characters."""
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n'), 'exclude': lambda f: f is None }})
    r"""The number of images to generate. Must be between 1 and 10."""
    response_format: Optional[CreateImageRequestResponseFormat] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response_format'), 'exclude': lambda f: f is None }})
    r"""The format in which the generated images are returned. Must be one of `url` or `b64_json`."""
    size: Optional[CreateImageRequestSize] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)."""
    

