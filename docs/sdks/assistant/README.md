# Assistant
(*assistant*)

### Available Operations

* [modify_assistant](#modify_assistant) - Modifies an assistant.

## modify_assistant

Modifies an assistant.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistant.modify_assistant(modify_assistant_request=components.ModifyAssistantRequest(
    file_ids=[
        'string',
    ],
    metadata=components.ModifyAssistantRequestMetadata(),
    tools=[
        components.CodeInterpreterTool(
            type=components.Type.CODE_INTERPRETER,
        ),
    ],
), assistant_id='string')

if res.assistant_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `modify_assistant_request`                                                             | [components.ModifyAssistantRequest](../../models/components/modifyassistantrequest.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `assistant_id`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | The ID of the assistant to modify.                                                     |


### Response

**[operations.ModifyAssistantResponse](../../models/operations/modifyassistantresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
