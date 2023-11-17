"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional

class Detail(str, Enum):
    r"""Specifies the detail level of the image."""
    AUTO = 'auto'
    LOW = 'low'
    HIGH = 'high'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ImageURL:
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""Either a URL of the image or the base64 encoded image data."""
    detail: Optional[Detail] = dataclasses.field(default=Detail.AUTO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    r"""Specifies the detail level of the image."""
    


class SchemasChatCompletionRequestMessageContentPartImageType(str, Enum):
    r"""The type of the content part."""
    IMAGE_URL = 'image_url'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ImageContentPart:
    image_url: ImageURL = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_url') }})
    type: SchemasChatCompletionRequestMessageContentPartImageType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the content part."""
    


class SchemasChatCompletionRequestMessageContentPartTextType(str, Enum):
    r"""The type of the content part."""
    TEXT = 'text'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TextContentPart:
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The text content."""
    type: SchemasChatCompletionRequestMessageContentPartTextType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the content part."""
    
