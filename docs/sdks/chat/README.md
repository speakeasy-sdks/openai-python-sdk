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
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateChatCompletionRequest(
    messages=[
        components.ChatCompletionRequestToolMessage(
            content='string',
            role=components.ChatCompletionRequestToolMessageRole.TOOL,
            tool_call_id='string',
        ),
    ],
    model=components.Two.GPT_3_5_TURBO,
    n=1,
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

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.CreateChatCompletionRequest](../../models/components/createchatcompletionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateChatCompletionResponse](../../models/operations/createchatcompletionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
