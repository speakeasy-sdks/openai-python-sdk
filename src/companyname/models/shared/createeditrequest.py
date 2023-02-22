import dataclasses
from companyname import utils
from dataclasses_json import dataclass_json
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class CreateEditRequest:
    instruction: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('instruction') }})
    model: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    input: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('input') }})
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('n') }})
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('temperature') }})
    top_p: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('top_p') }})
    