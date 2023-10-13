# Moderations
(*moderations*)

## Overview

Given a input text, outputs if the model classifies it as violating OpenAI's content policy.

### Available Operations

* [create_moderation](#create_moderation) - Classifies if text violates OpenAI's Content Policy

## create_moderation

Classifies if text violates OpenAI's Content Policy

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateModerationRequest(
    [
        'I',
        ' ',
        'w',
        'a',
        'n',
        't',
        ' ',
        't',
        'o',
        ' ',
        'k',
        'i',
        'l',
        'l',
        ' ',
        't',
        'h',
        'e',
        'm',
        '.',
    ],
shared.CreateModerationRequestModel2.TEXT_MODERATION_STABLE,
)

res = s.moderations.create_moderation(req)

if res.create_moderation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.CreateModerationRequest](../../models/shared/createmoderationrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateModerationResponse](../../models/operations/createmoderationresponse.md)**

