from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from openai import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAnswerResponseSelectedDocuments:
    document: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('document'), 'exclude': lambda f: f is None }})
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('text'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAnswerResponse:
    answers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('answers'), 'exclude': lambda f: f is None }})
    completion: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completion'), 'exclude': lambda f: f is None }})
    model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('model'), 'exclude': lambda f: f is None }})
    object: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object'), 'exclude': lambda f: f is None }})
    search_model: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_model'), 'exclude': lambda f: f is None }})
    selected_documents: Optional[list[CreateAnswerResponseSelectedDocuments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selected_documents'), 'exclude': lambda f: f is None }})
    