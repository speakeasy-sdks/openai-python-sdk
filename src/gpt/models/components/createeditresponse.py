"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .completionusage import CompletionUsage
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import List

class CreateEditResponseFinishReason(str, Enum):
    r"""The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    or `content_filter` if content was omitted due to a flag from our content filters.
    """
    STOP = 'stop'
    LENGTH = 'length'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponseChoices:
    finish_reason: CreateEditResponseFinishReason = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finish_reason') }})
    r"""The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    or `content_filter` if content was omitted due to a flag from our content filters.
    """
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""The index of the choice in the list of choices."""
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The edited result."""
    


class CreateEditResponseObject(str, Enum):
    r"""The object type, which is always `edit`."""
    EDIT = 'edit'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponse:
    r"""Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible."""
    choices: List[CreateEditResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices') }})
    r"""A list of edit choices. Can be more than one if `n` is greater than 1."""
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    r"""The Unix timestamp (in seconds) of when the edit was created."""
    object: CreateEditResponseObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    r"""The object type, which is always `edit`."""
    usage: CompletionUsage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    r"""Usage statistics for the completion request."""
    

