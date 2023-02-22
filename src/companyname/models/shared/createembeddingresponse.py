import dataclasses
from companyname import utils
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class CreateEmbeddingResponseData:
    embedding: list[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('embedding') }})
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEmbeddingResponseUsage:
    prompt_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt_tokens') }})
    total_tokens: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total_tokens') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEmbeddingResponse:
    data: list[CreateEmbeddingResponseData] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('model') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    usage: CreateEmbeddingResponseUsage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('usage') }})
    