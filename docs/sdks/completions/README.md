# Completions
(*completions*)

## Overview

Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.

### Available Operations

* [create_completion](#create_completion) - Creates a completion for the provided prompt and parameters.

## create_completion

Creates a completion for the provided prompt and parameters.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateCompletionRequest(
    logit_bias={
        "key": 160667,
    },
    max_tokens=16,
'string',
    n=1,
'This is a test.',
'
',
    suffix='test.',
    temperature=1,
    top_p=1,
    user='user-1234',
)

res = s.completions.create_completion(req)

if res.create_completion_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.CreateCompletionRequest](../../models/components/createcompletionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateCompletionResponse](../../models/operations/createcompletionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
