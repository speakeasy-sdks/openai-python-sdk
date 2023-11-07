"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ToolOutputs:
    output: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output'), 'exclude': lambda f: f is None }})
    r"""The output of the tool call to be submitted to continue the run."""
    tool_call_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool_call_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the tool call in the `required_action` object within the run object the output is being submitted for."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmitToolOutputsRunRequest:
    tool_outputs: List[ToolOutputs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool_outputs') }})
    r"""A list of tools for which the outputs are being submitted."""
    

