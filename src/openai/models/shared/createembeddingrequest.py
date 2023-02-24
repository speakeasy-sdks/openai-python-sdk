from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from openai import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEmbeddingRequest:
    input: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('input') }})
    model: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    