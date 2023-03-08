from __future__ import annotations
import dataclasses
from ..shared import chatcompletionresponsemessage as shared_chatcompletionresponsemessage
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateChatCompletionResponseChoices:
    finish_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finish_reason'), 'exclude': lambda f: f is None }})
    index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index'), 'exclude': lambda f: f is None }})
    message: Optional[shared_chatcompletionresponsemessage.ChatCompletionResponseMessage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateChatCompletionResponseUsage:
    completion_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_tokens') }})
    prompt_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt_tokens') }})
    total_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_tokens') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateChatCompletionResponse:
    choices: list[CreateChatCompletionResponseChoices] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('choices') }})
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    usage: Optional[CreateChatCompletionResponseUsage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usage'), 'exclude': lambda f: f is None }})
    