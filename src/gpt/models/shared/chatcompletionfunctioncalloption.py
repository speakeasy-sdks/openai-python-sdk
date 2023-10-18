"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionFunctionCallOption:
    r"""Controls how the model calls functions. \\"none\\" means the model will not call a function and instead generates a message. \\"auto\\" means the model can pick between generating a message or calling a function.  Specifying a particular function via `{\\"name\\": \\"my_function\\"}` forces the model to call that function. \\"none\\" is the default when no functions are present. \\"auto\\" is the default if functions are present."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the function to call."""
    

