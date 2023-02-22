import dataclasses
from dataclasses_json import dataclass_json
from openai import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class CreateEditResponseChoicesLogprobs:
    text_offset: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('text_offset') }})
    token_logprobs: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('token_logprobs') }})
    tokens: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tokens') }})
    top_logprobs: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('top_logprobs') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEditResponseChoices:
    finish_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('finish_reason') }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    logprobs: Optional[CreateEditResponseChoicesLogprobs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logprobs') }})
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('text') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEditResponseUsage:
    completion_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('completion_tokens') }})
    prompt_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt_tokens') }})
    total_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total_tokens') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEditResponse:
    choices: list[CreateEditResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('choices') }})
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    usage: CreateEditResponseUsage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('usage') }})
    