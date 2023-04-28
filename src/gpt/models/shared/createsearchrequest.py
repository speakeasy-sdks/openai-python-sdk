"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from gpt import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSearchRequest:
    
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})

    r"""Query to search against the documents."""
    documents: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documents'), 'exclude': lambda f: f is None }})

    r"""Up to 200 documents to search over, provided as a list of strings.
    
    The maximum document length (in tokens) is 2034 minus the number of tokens in the query.
    
    You should specify either `documents` or a `file`, but not both.
    """
    file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file'), 'exclude': lambda f: f is None }})

    r"""The ID of an uploaded file that contains documents to search over.
    
    You should specify either `documents` or a `file`, but not both.
    """
    max_rerank: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_rerank'), 'exclude': lambda f: f is None }})

    r"""The maximum number of documents to be re-ranked and returned by search.
    
    This flag only takes effect when `file` is set.
    """
    return_metadata: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('return_metadata'), 'exclude': lambda f: f is None }})

    r"""A special boolean flag for showing metadata. If set to `true`, each document entry in the returned JSON will contain a \\"metadata\\" field.
    
    This flag only takes effect when `file` is set.
    """
    user: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})

    