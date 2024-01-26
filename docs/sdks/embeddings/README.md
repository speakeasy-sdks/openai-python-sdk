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
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateEmbeddingRequest(
    encoding_format=components.EncodingFormat.FLOAT,
    input='The quick brown fox jumped over the lazy dog',
    model=components.CreateEmbeddingRequest2.TEXT_EMBEDDING_3_SMALL,
    user='user-1234',
)

res = s.embeddings.create_embedding(req)

if res.create_embedding_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateEmbeddingRequest](../../models/components/createembeddingrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateEmbeddingResponse](../../models/operations/createembeddingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
