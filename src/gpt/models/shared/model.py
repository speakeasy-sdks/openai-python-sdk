"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Model:
    r"""OK"""
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    object: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    owned_by: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owned_by') }})
    

