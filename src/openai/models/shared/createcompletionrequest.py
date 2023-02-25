from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from openai import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCompletionRequest:
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    best_of: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('best_of'), 'exclude': lambda f: f is None }})
    echo: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('echo'), 'exclude': lambda f: f is None }})
    frequency_penalty: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency_penalty'), 'exclude': lambda f: f is None }})
    logit_bias: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logit_bias'), 'exclude': lambda f: f is None }})
    logprobs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logprobs'), 'exclude': lambda f: f is None }})
    max_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('max_tokens'), 'exclude': lambda f: f is None }})
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('n'), 'exclude': lambda f: f is None }})
    presence_penalty: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('presence_penalty'), 'exclude': lambda f: f is None }})
    prompt: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt'), 'exclude': lambda f: f is None }})
    stop: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('stop'), 'exclude': lambda f: f is None }})
    stream: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('stream'), 'exclude': lambda f: f is None }})
    suffix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suffix'), 'exclude': lambda f: f is None }})
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('temperature'), 'exclude': lambda f: f is None }})
    top_p: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('top_p'), 'exclude': lambda f: f is None }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    