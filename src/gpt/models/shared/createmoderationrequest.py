"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import List, Optional, Union


@dataclasses.dataclass
class CreateModerationRequestInput:
    pass

class CreateModerationRequestModel2(str, Enum):
    r"""Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

    The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.
    """
    TEXT_MODERATION_LATEST = 'text-moderation-latest'
    TEXT_MODERATION_STABLE = 'text-moderation-stable'


@dataclasses.dataclass
class CreateModerationRequestModel:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModerationRequest:
    input: Union[str, List[str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})
    r"""The input text to classify"""
    model: Optional[Union[str, CreateModerationRequestModel2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model'), 'exclude': lambda f: f is None }})
    r"""Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

    The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.
    """
    

