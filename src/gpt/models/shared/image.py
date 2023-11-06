"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Image:
    r"""Represents the url or the content of an image generated by the OpenAI API."""
    b64_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('b64_json'), 'exclude': lambda f: f is None }})
    r"""The base64-encoded JSON of the generated image, if `response_format` is `b64_json`."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""The URL of the generated image, if `response_format` is `url` (default)."""
    

