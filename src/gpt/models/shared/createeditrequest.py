"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union

class CreateEditRequestModel2(str, Enum):
    r"""ID of the model to use. You can use the `text-davinci-edit-001` or `code-davinci-edit-001` model with this endpoint."""
    TEXT_DAVINCI_EDIT_001 = 'text-davinci-edit-001'
    CODE_DAVINCI_EDIT_001 = 'code-davinci-edit-001'


@dataclasses.dataclass
class CreateEditRequestModel:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateEditRequest:
    instruction: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instruction') }})
    r"""The instruction that tells the model how to edit the prompt."""
    model: Union[str, CreateEditRequestModel2] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""ID of the model to use. You can use the `text-davinci-edit-001` or `code-davinci-edit-001` model with this endpoint."""
    input: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})
    r"""The input text to use as a starting point for the edit."""
    n: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n') }})
    r"""How many edits to generate for the input and instruction."""
    temperature: Optional[float] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature') }})
    r"""What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """
    top_p: Optional[float] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_p') }})
    r"""An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """
    

