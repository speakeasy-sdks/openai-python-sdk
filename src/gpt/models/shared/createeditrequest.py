from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditRequest:
    instruction: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instruction') }})
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    input: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input'), 'exclude': lambda f: f is None }})
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n'), 'exclude': lambda f: f is None }})
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature'), 'exclude': lambda f: f is None }})
    top_p: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_p'), 'exclude': lambda f: f is None }})
    