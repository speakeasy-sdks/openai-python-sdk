"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .runobject import RunObject
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListRunsResponse:
    data: List[RunObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    first_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_id') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more') }})
    last_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_id') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    

