"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils

class MessageFileObjectObject(str, Enum):
    r"""The object type, which is always `thread.message.file`."""
    THREAD_MESSAGE_FILE = 'thread.message.file'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MessageFileObject:
    r"""A list of files attached to a `message`."""
    created_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at') }})
    r"""The Unix timestamp (in seconds) for when the message file was created."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The identifier, which can be referenced in API endpoints."""
    message_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_id') }})
    r"""The ID of the [message](/docs/api-reference/messages) that the [File](/docs/api-reference/files) is attached to."""
    object: MessageFileObjectObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object') }})
    r"""The object type, which is always `thread.message.file`."""
    

