"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assistanttoolscode import AssistantToolsCode
from .assistanttoolsfunction import AssistantToolsFunction
from .assistanttoolsretrieval import AssistantToolsRetrieval
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import List, Optional, Union


@dataclasses.dataclass
class CreateRunRequestMetadata:
    r"""Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateRunRequest:
    assistant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assistant_id') }})
    r"""The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run."""
    instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instructions') }})
    r"""Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis."""
    metadata: Optional[CreateRunRequestMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long."""
    model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used."""
    tools: Optional[List[Union[AssistantToolsCode, AssistantToolsRetrieval, AssistantToolsFunction]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tools') }})
    r"""Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis."""
    

