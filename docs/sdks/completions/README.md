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
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateCompletionRequest(
    logit_bias={
        "red": 242695,
    },
    max_tokens=16,
'optimistic',
    n=1,
    [
        [,
        1,
        2,
        1,
        2,
        ,,
         ,
        3,
        1,
        8,
        ,,
         ,
        2,
        5,
        7,
        ,,
         ,
        1,
        3,
        3,
        2,
        ,,
         ,
        1,
        3,
        ],
    ],
    [
        '[',
        '"',
        '\',
        'n',
        '"',
        ']',
    ],
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

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.CreateCompletionRequest](../../models/shared/createcompletionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateCompletionResponse](../../models/operations/createcompletionresponse.md)**

