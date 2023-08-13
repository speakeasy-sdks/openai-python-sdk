"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import completionusage as shared_completionusage
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional

class CreateCompletionResponseChoicesFinishReason(str, Enum):
    r"""The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    or `length` if the maximum number of tokens specified in the request was reached.
    """
    STOP = 'stop'
    LENGTH = 'length'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponseChoicesLogprobs:
    text_offset: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_offset'), 'exclude': lambda f: f is None }})
    token_logprobs: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_logprobs'), 'exclude': lambda f: f is None }})
    tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokens'), 'exclude': lambda f: f is None }})
    top_logprobs: Optional[list[dict[str, int]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_logprobs'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponseChoices:
    finish_reason: CreateCompletionResponseChoicesFinishReason = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finish_reason') }})
    r"""The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    or `length` if the maximum number of tokens specified in the request was reached.
    """
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    logprobs: CreateCompletionResponseChoicesLogprobs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logprobs') }})
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponse:
    r"""Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint)."""
    choices: list[CreateCompletionResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices') }})
    r"""The list of completion choices the model generated for the input prompt."""
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    r"""The Unix timestamp of when the completion was created."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique identifier for the completion."""
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The model used for completion."""
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    r"""The object type, which is always \\"text_completion\\" """
    usage: Optional[shared_completionusage.CompletionUsage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage'), 'exclude': lambda f: f is None }})
    r"""Usage statistics for the completion request."""
    

