from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationRequest:
    input: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})
    model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model'), 'exclude': lambda f: f is None }})
    