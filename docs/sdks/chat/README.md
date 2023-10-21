# Chat
(*chat*)

## Overview

Given a list of messages comprising a conversation, the model will return a response.

### Available Operations

* [create_chat_completion](#create_chat_completion) - Creates a model response for the given chat conversation.

## create_chat_completion

Creates a model response for the given chat conversation.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateChatCompletionRequest(
    shared.ChatCompletionFunctionCallOption(
        name='string',
    ),
    functions=[
        shared.ChatCompletionFunctions(
            name='string',
            parameters={
                "key": 'string',
            },
        ),
    ],
    logit_bias={
        "key": 544683,
    },
    messages=[
        shared.ChatCompletionRequestMessage(
            content='string',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='string',
                name='string',
            ),
            role=shared.ChatCompletionRequestMessageRole.USER,
        ),
    ],
shared.CreateChatCompletionRequestModel2.GPT_3_5_TURBO,
    n=1,
    [
        'string',
    ],
    temperature=1,
    top_p=1,
    user='user-1234',
)

res = s.chat.create_chat_completion(req)

if res.create_chat_completion_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateChatCompletionRequest](../../models/shared/createchatcompletionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateChatCompletionResponse](../../models/operations/createchatcompletionresponse.md)**

