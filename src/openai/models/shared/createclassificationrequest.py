from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from openai import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateClassificationRequest:
    model: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('query') }})
    examples: Optional[list[list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('examples'), 'exclude': lambda f: f is None }})
    expand: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expand'), 'exclude': lambda f: f is None }})
    file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('file'), 'exclude': lambda f: f is None }})
    labels: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labels'), 'exclude': lambda f: f is None }})
    logit_bias: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logit_bias'), 'exclude': lambda f: f is None }})
    logprobs: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logprobs'), 'exclude': lambda f: f is None }})
    max_examples: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('max_examples'), 'exclude': lambda f: f is None }})
    return_metadata: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('return_metadata'), 'exclude': lambda f: f is None }})
    return_prompt: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('return_prompt'), 'exclude': lambda f: f is None }})
    search_model: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_model'), 'exclude': lambda f: f is None }})
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('temperature'), 'exclude': lambda f: f is None }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    