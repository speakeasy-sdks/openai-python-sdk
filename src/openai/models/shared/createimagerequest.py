from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from openai import utils
from typing import Any, Optional

class CreateImageRequestResponseFormatEnum(str, Enum):
    URL = "url"
    B64_JSON = "b64_json"

class CreateImageRequestSizeEnum(str, Enum):
    TWO_HUNDRED_AND_FIFTY_SIXX256 = "256x256"
    FIVE_HUNDRED_AND_TWELVEX512 = "512x512"
    ONE_THOUSAND_AND_TWENTY_FOURX1024 = "1024x1024"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateImageRequest:
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('prompt') }})
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('n'), 'exclude': lambda f: f is None }})
    response_format: Optional[CreateImageRequestResponseFormatEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('response_format'), 'exclude': lambda f: f is None }})
    size: Optional[CreateImageRequestSizeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('size'), 'exclude': lambda f: f is None }})
    user: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    