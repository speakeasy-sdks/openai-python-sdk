from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from openai import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSearchResponseData:
    document: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('document'), 'exclude': lambda f: f is None }})
    object: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object'), 'exclude': lambda f: f is None }})
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('score'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSearchResponse:
    data: Optional[list[CreateSearchResponseData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('model'), 'exclude': lambda f: f is None }})
    object: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object'), 'exclude': lambda f: f is None }})
    