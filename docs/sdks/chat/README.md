# Chat
(*.chat*)

## Overview

Given a list of messages comprising a conversation, the model will return a response.

### Available Operations

* [create_chat_completion](#create_chat_completion) - Creates a model response for the given chat conversation.

## create_chat_completion

Creates a model response for the given chat conversation.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateChatCompletionRequest(
    components.Schemas(
        name='string',
    ),
    functions=[
        components.ChatCompletionFunctions(
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
        components.UserMessage(
            [
                components.TextContentPart(
                    text='string',
                    type=components.SchemasChatCompletionRequestMessageContentPartTextType.TEXT,
                ),
            ],
            role=components.SchemasChatCompletionRequestUserMessageRole.USER,
        ),
    ],
components.Two.GPT_3_5_TURBO,
    n=1,
    response_format=components.ResponseFormat(
        type=components.CreateChatCompletionRequestType.JSON_OBJECT,
    ),
'string',
    temperature=1,
components.ChatCompletionToolChoiceOption1.NONE,
    tools=[
        components.ChatCompletionTool(
            function=components.ChatCompletionToolFunction(
                name='string',
                parameters={
                    "key": 'string',
                },
            ),
            type=components.ChatCompletionToolType.FUNCTION,
        ),
    ],
    top_p=1,
    user='user-1234',
)

res = s.chat.create_chat_completion(req)

if res.create_chat_completion_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.CreateChatCompletionRequest](../../models/shared/createchatcompletionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateChatCompletionResponse](../../models/operations/createchatcompletionresponse.md)**

