"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional

class ChatCompletionRequestMessageRole(str, Enum):
    r"""The role of the author of this message."""
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ChatCompletionRequestMessage:
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""The contents of the message"""
    role: ChatCompletionRequestMessageRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role of the author of this message."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the user in a multi-user chat"""
    

