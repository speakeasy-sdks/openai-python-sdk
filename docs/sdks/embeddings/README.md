# Embeddings
(*embeddings*)

## Overview

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

### Available Operations

* [create_embedding](#create_embedding) - Creates an embedding vector representing the input text.

## create_embedding

Creates an embedding vector representing the input text.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateEmbeddingRequest(
    encoding_format=shared.CreateEmbeddingRequestEncodingFormat.FLOAT,
'The quick brown fox jumped over the lazy dog',
shared.CreateEmbeddingRequestModel2.TEXT_EMBEDDING_ADA_002,
    user='user-1234',
)

res = s.embeddings.create_embedding(req)

if res.create_embedding_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateEmbeddingRequest](../../models/shared/createembeddingrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateEmbeddingResponse](../../models/operations/createembeddingresponse.md)**

