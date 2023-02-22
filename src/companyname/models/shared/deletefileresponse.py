import dataclasses
from companyname import utils
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class DeleteFileResponse:
    deleted: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    