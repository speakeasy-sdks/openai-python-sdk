"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union



@dataclasses.dataclass
class CreateEmbeddingRequestInput:
    pass

class CreateEmbeddingRequestModel2(str, Enum):
    r"""ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them."""
    TEXT_EMBEDDING_ADA_002 = 'text-embedding-ada-002'



@dataclasses.dataclass
class CreateEmbeddingRequestModel:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateEmbeddingRequest:
    input: Union[str, list[str], list[int], list[list[int]]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input') }})
    r"""Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. Each input must not exceed the max input tokens for the model (8191 tokens for `text-embedding-ada-002`) and cannot be an empty string. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens."""
    model: Union[str, CreateEmbeddingRequestModel2] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them."""
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)."""
    

