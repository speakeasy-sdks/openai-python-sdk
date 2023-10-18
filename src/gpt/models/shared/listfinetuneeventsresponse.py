"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import finetuneevent as shared_finetuneevent
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListFineTuneEventsResponse:
    data: List[shared_finetuneevent.FineTuneEvent] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    

