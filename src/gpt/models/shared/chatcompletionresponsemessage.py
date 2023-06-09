"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils

class ChatCompletionResponseMessageRole(str, Enum):
    r"""The role of the author of this message."""
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionResponseMessage:
    
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""The contents of the message"""
    role: ChatCompletionResponseMessageRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role of the author of this message."""
    