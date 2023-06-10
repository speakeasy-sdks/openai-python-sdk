"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateEditRequest:
    instruction: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instruction') }})
    r"""The instruction that tells the model how to edit the prompt."""
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""ID of the model to use. You can use the `text-davinci-edit-001` or `code-davinci-edit-001` model with this endpoint."""
    input: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input'), 'exclude': lambda f: f is None }})
    r"""The input text to use as a starting point for the edit."""
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n'), 'exclude': lambda f: f is None }})
    r"""How many edits to generate for the input and instruction."""
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature'), 'exclude': lambda f: f is None }})
    r"""completions_temperature_description"""
    top_p: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_p'), 'exclude': lambda f: f is None }})
    r"""completions_top_p_description"""
    

