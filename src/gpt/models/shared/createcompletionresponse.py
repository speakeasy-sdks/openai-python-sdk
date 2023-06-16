"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional



@dataclasses.dataclass
class CreateCompletionResponseChoicesLogprobsTopLogprobs:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponseChoicesLogprobs:
    text_offset: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_offset'), 'exclude': lambda f: f is None }})
    token_logprobs: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_logprobs'), 'exclude': lambda f: f is None }})
    tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokens'), 'exclude': lambda f: f is None }})
    top_logprobs: Optional[list[CreateCompletionResponseChoicesLogprobsTopLogprobs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_logprobs'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponseChoices:
    finish_reason: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finish_reason') }})
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    logprobs: CreateCompletionResponseChoicesLogprobs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logprobs') }})
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponseUsage:
    completion_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_tokens') }})
    prompt_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt_tokens') }})
    total_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_tokens') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCompletionResponse:
    r"""OK"""
    choices: list[CreateCompletionResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices') }})
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    usage: Optional[CreateCompletionResponseUsage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage'), 'exclude': lambda f: f is None }})
    

