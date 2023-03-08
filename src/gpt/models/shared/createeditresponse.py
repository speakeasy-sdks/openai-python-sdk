from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponseChoicesLogprobs:
    text_offset: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_offset'), 'exclude': lambda f: f is None }})
    token_logprobs: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_logprobs'), 'exclude': lambda f: f is None }})
    tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokens'), 'exclude': lambda f: f is None }})
    top_logprobs: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_logprobs'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponseChoices:
    finish_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finish_reason'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index'), 'exclude': lambda f: f is None }})
    logprobs: Optional[CreateEditResponseChoicesLogprobs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logprobs'), 'exclude': lambda f: f is None }})
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponseUsage:
    completion_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_tokens') }})
    prompt_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt_tokens') }})
    total_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_tokens') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditResponse:
    choices: list[CreateEditResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices') }})
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    usage: CreateEditResponseUsage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage') }})
    