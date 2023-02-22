import dataclasses
from dataclasses_json import dataclass_json
from openai import utils
from typing import Any


@dataclass_json
@dataclasses.dataclass
class ListModelsResponse:
    data: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    