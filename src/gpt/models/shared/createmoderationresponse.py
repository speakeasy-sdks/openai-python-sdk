from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationResponseResultsCategories:
    hate: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hate') }})
    hate_threatening: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hate/threatening') }})
    self_harm: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self-harm') }})
    sexual: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexual') }})
    sexual_minors: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexual/minors') }})
    violence: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violence') }})
    violence_graphic: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violence/graphic') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationResponseResultsCategoryScores:
    hate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hate') }})
    hate_threatening: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hate/threatening') }})
    self_harm: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self-harm') }})
    sexual: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexual') }})
    sexual_minors: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexual/minors') }})
    violence: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violence') }})
    violence_graphic: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violence/graphic') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationResponseResults:
    categories: CreateModerationResponseResultsCategories = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categories') }})
    category_scores: CreateModerationResponseResultsCategoryScores = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category_scores') }})
    flagged: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flagged') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationResponse:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    results: list[CreateModerationResponseResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    