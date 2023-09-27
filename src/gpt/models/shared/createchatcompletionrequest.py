"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import chatcompletionfunctioncalloption as shared_chatcompletionfunctioncalloption
from ..shared import chatcompletionfunctions as shared_chatcompletionfunctions
from ..shared import chatcompletionrequestmessage as shared_chatcompletionrequestmessage
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from gpt import utils
from typing import Optional, Union

class CreateChatCompletionRequestFunctionCall1(str, Enum):
    r"""Controls how the model responds to function calls. `none` means the model does not call a function, and responds to the end-user. `auto` means the model can pick between an end-user or calling a function.  Specifying a particular function via `{\\"name\\": \\"my_function\\"}` forces the model to call that function. `none` is the default when no functions are present. `auto` is the default if functions are present."""
    NONE = 'none'
    AUTO = 'auto'



@dataclasses.dataclass
class CreateChatCompletionRequestFunctionCall:
    pass

class CreateChatCompletionRequestModel2(str, Enum):
    r"""ID of the model to use. See the [model endpoint compatibility](/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API."""
    GPT_4 = 'gpt-4'
    GPT_4_0314 = 'gpt-4-0314'
    GPT_4_0613 = 'gpt-4-0613'
    GPT_4_32K = 'gpt-4-32k'
    GPT_4_32K_0314 = 'gpt-4-32k-0314'
    GPT_4_32K_0613 = 'gpt-4-32k-0613'
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_16K = 'gpt-3.5-turbo-16k'
    GPT_3_5_TURBO_0301 = 'gpt-3.5-turbo-0301'
    GPT_3_5_TURBO_0613 = 'gpt-3.5-turbo-0613'
    GPT_3_5_TURBO_16K_0613 = 'gpt-3.5-turbo-16k-0613'



@dataclasses.dataclass
class CreateChatCompletionRequestModel:
    pass



@dataclasses.dataclass
class CreateChatCompletionRequestStop:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateChatCompletionRequest:
    messages: list[shared_chatcompletionrequestmessage.ChatCompletionRequestMessage] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messages') }})
    r"""A list of messages comprising the conversation so far. [Example Python code](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)."""
    model: Union[str, CreateChatCompletionRequestModel2] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})
    r"""ID of the model to use. See the [model endpoint compatibility](/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API."""
    frequency_penalty: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency_penalty'), 'exclude': lambda f: f is None }})
    r"""Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

    [See more information about frequency and presence penalties.](/docs/guides/gpt/parameter-details)
    """
    function_call: Optional[Union[CreateChatCompletionRequestFunctionCall1, shared_chatcompletionfunctioncalloption.ChatCompletionFunctionCallOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('function_call'), 'exclude': lambda f: f is None }})
    r"""Controls how the model responds to function calls. `none` means the model does not call a function, and responds to the end-user. `auto` means the model can pick between an end-user or calling a function.  Specifying a particular function via `{\\"name\\": \\"my_function\\"}` forces the model to call that function. `none` is the default when no functions are present. `auto` is the default if functions are present."""
    functions: Optional[list[shared_chatcompletionfunctions.ChatCompletionFunctions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('functions'), 'exclude': lambda f: f is None }})
    r"""A list of functions the model may generate JSON inputs for."""
    logit_bias: Optional[dict[str, int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logit_bias'), 'exclude': lambda f: f is None }})
    r"""Modify the likelihood of specified tokens appearing in the completion.

    Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.
    """
    max_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_tokens'), 'exclude': lambda f: f is None }})
    r"""The maximum number of [tokens](/tokenizer) to generate in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb) for counting tokens.
    """
    n: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('n'), 'exclude': lambda f: f is None }})
    r"""How many chat completion choices to generate for each input message."""
    presence_penalty: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('presence_penalty'), 'exclude': lambda f: f is None }})
    r"""Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

    [See more information about frequency and presence penalties.](/docs/guides/gpt/parameter-details)
    """
    stop: Optional[Union[str, list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stop'), 'exclude': lambda f: f is None }})
    r"""Up to 4 sequences where the API will stop generating further tokens."""
    stream: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream'), 'exclude': lambda f: f is None }})
    r"""If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb)."""
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature'), 'exclude': lambda f: f is None }})
    r"""What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """
    top_p: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('top_p'), 'exclude': lambda f: f is None }})
    r"""An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids)."""
    

