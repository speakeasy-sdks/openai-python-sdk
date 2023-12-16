"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assistanttoolscode import AssistantToolsCode
from .assistanttoolsfunction import AssistantToolsFunction
from .assistanttoolsretrieval import AssistantToolsRetrieval
from .runtoolcallobject import RunToolCallObject
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import List, Optional, Union

class Code(str, Enum):
    r"""One of `server_error` or `rate_limit_exceeded`."""
    SERVER_ERROR = 'server_error'
    RATE_LIMIT_EXCEEDED = 'rate_limit_exceeded'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LastError:
    r"""The last error associated with this run. Will be `null` if there are no errors."""
    code: Code = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    r"""One of `server_error` or `rate_limit_exceeded`."""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human-readable description of the error."""
    



@dataclasses.dataclass
class RunObjectMetadata:
    r"""Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long."""
    


class RunObjectObject(str, Enum):
    r"""The object type, which is always `thread.run`."""
    THREAD_RUN = 'thread.run'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmitToolOutputs:
    r"""Details on the tool outputs needed for this run to continue."""
    tool_calls: List[RunToolCallObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool_calls') }})
    r"""A list of the relevant tool calls."""
    


class RunObjectType(str, Enum):
    r"""For now, this is always `submit_tool_outputs`."""
    SUBMIT_TOOL_OUTPUTS = 'submit_tool_outputs'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RequiredAction:
    r"""Details on the action required to continue the run. Will be `null` if no action is required."""
    submit_tool_outputs: SubmitToolOutputs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submit_tool_outputs') }})
    r"""Details on the tool outputs needed for this run to continue."""
    type: RunObjectType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""For now, this is always `submit_tool_outputs`."""
    


class RunObjectStatus(str, Enum):
    r"""The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`."""
    QUEUED = 'queued'
    IN_PROGRESS = 'in_progress'
    REQUIRES_ACTION = 'requires_action'
    CANCELLING = 'cancelling'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    COMPLETED = 'completed'
    EXPIRED = 'expired'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RunObject:
    r"""Represents an execution run on a [thread](/docs/api-reference/threads)."""
    assistant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assistant_id') }})
    r"""The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run."""
    cancelled_at: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancelled_at') }})
    r"""The Unix timestamp (in seconds) for when the run was cancelled."""
    completed_at: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completed_at') }})
    r"""The Unix timestamp (in seconds) for when the run was completed."""
    created_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at') }})
    r"""The Unix timestamp (in seconds) for when the run was created."""
    expires_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at') }})
    r"""The Unix timestamp (in seconds) for when the run will expire."""
    failed_at: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_at') }})
    r"""The Unix timestamp (in seconds) for when the run failed."""
    file_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_ids') }})
    r"""The list of [File](/docs/api-reference/files) IDs the [assistant](/docs/api-reference/assistants) used for this run."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The identifier, which can be referenced in API endpoints."""
    instructions: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instructions') }})
    r"""The instructions that the [assistant](/docs/api-reference/assistants) used for this run."""
    last_error: Optional[LastError] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_error') }})
    r"""The last error associated with this run. Will be `null` if there are no errors."""
    metadata: Optional[RunObjectMetadata] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long."""
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""The model that the [assistant](/docs/api-reference/assistants) used for this run."""
    object: RunObjectObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    r"""The object type, which is always `thread.run`."""
    required_action: Optional[RequiredAction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required_action') }})
    r"""Details on the action required to continue the run. Will be `null` if no action is required."""
    started_at: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('started_at') }})
    r"""The Unix timestamp (in seconds) for when the run was started."""
    status: RunObjectStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`."""
    thread_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('thread_id') }})
    r"""The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run."""
    tools: List[Union[AssistantToolsCode, AssistantToolsRetrieval, AssistantToolsFunction]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tools') }})
    r"""The list of tools that the [assistant](/docs/api-reference/assistants) used for this run."""
    

