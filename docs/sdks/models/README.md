# Models
(*models*)

## Overview

List and describe the various models available in the API.

### Available Operations

* [delete_model](#delete_model) - Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
* [list_models](#list_models) - Lists the currently available models, and provides basic information about each one such as the owner and availability.
* [retrieve_model](#retrieve_model) - Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

## delete_model

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.DeleteModelRequest(
    model='ft:gpt-3.5-turbo:acemeco:suffix:abc123',
)

res = s.models.delete_model(req)

if res.delete_model_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.DeleteModelRequest](../../models/operations/deletemodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteModelResponse](../../models/operations/deletemodelresponse.md)**


## list_models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.models.list_models()

if res.list_models_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListModelsResponse](../../models/operations/listmodelsresponse.md)**


## retrieve_model

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.RetrieveModelRequest(
    model='gpt-3.5-turbo',
)

res = s.models.retrieve_model(req)

if res.model is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RetrieveModelRequest](../../models/operations/retrievemodelrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RetrieveModelResponse](../../models/operations/retrievemodelresponse.md)**
