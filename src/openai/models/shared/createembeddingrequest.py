import dataclasses
from dataclasses_json import dataclass_json
from openai import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class CreateEmbeddingRequest:
    input: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('input') }})
    model: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user') }})
    