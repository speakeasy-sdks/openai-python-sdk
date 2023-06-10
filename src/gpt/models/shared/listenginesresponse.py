"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import engine as shared_engine
from dataclasses_json import Undefined, dataclass_json
from gpt import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListEnginesResponse:
    r"""OK"""
    data: list[shared_engine.Engine] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    

