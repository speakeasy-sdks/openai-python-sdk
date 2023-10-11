# Edits
(*edits*)

## Overview

Given a prompt and an instruction, the model will return an edited version of the prompt.

### Available Operations

* [~~create_edit~~](#create_edit) - Creates a new edit for the provided input, instruction, and parameters. :warning: **Deprecated**

## ~~create_edit~~

Creates a new edit for the provided input, instruction, and parameters.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateEditRequest(
    input='What day of the wek is it?',
    instruction='Fix the spelling mistakes.',
shared.CreateEditRequestModel2.TEXT_DAVINCI_EDIT_001,
    n=1,
    temperature=1,
    top_p=1,
)

res = s.edits.create_edit(req)

if res.create_edit_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateEditRequest](../../models/shared/createeditrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateEditResponse](../../models/operations/createeditresponse.md)**

