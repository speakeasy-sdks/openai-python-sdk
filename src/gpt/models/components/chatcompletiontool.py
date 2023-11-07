"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionToolFunction:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""
    parameters: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    r"""The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/gpt/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

    To describe a function that accepts no parameters, provide the value `{\"type\": \"object\", \"properties\": {}}`.
    """
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""A description of what the function does, used by the model to choose when and how to call the function."""
    


class ChatCompletionToolType(str, Enum):
    r"""The type of the tool. Currently, only `function` is supported."""
    FUNCTION = 'function'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionTool:
    function: ChatCompletionToolFunction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('function') }})
    type: ChatCompletionToolType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the tool. Currently, only `function` is supported."""
    

