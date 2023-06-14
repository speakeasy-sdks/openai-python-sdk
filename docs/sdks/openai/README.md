# open_ai

## Overview

The OpenAI REST API

### Available Operations

* [cancel_fine_tune](#cancel_fine_tune) - Immediately cancel a fine-tune job.

* [~~create_answer~~](#create_answer) - Answers the specified question using the provided documents and examples.

The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions).
 :warning: **Deprecated**
* [create_chat_completion](#create_chat_completion) - Creates a model response for the given chat conversation.
* [~~create_classification~~](#create_classification) - Classifies the specified `query` using provided examples.

The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
to select the ones most relevant for the particular query. Then, the relevant examples
are combined with the query to construct a prompt to produce the final label via the
[completions](/docs/api-reference/completions) endpoint.

Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
request using the `examples` parameter for quick tests and small scale use cases.
 :warning: **Deprecated**
* [create_completion](#create_completion) - Creates a completion for the provided prompt and parameters.
* [create_edit](#create_edit) - Creates a new edit for the provided input, instruction, and parameters.
* [create_embedding](#create_embedding) - Creates an embedding vector representing the input text.
* [create_file](#create_file) - Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.

* [create_fine_tune](#create_fine_tune) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about Fine-tuning](/docs/guides/fine-tuning)

* [create_image](#create_image) - Creates an image given a prompt.
* [create_image_edit](#create_image_edit) - Creates an edited or extended image given an original image and a prompt.
* [create_image_variation](#create_image_variation) - Creates a variation of a given image.
* [create_moderation](#create_moderation) - Classifies if text violates OpenAI's Content Policy
* [~~create_search~~](#create_search) - The search endpoint computes similarity scores between provided query and documents. Documents can be passed directly to the API if there are no more than 200 of them.

To go beyond the 200 document limit, documents can be processed offline and then used for efficient retrieval at query time. When `file` is set, the search endpoint searches over all the documents in the given file and returns up to the `max_rerank` number of documents. These documents will be returned along with their search scores.

The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go higher), where a score above 200 usually means the document is semantically similar to the query.
 :warning: **Deprecated**
* [create_transcription](#create_transcription) - Transcribes audio into the input language.
* [create_translation](#create_translation) - Translates audio into into English.
* [delete_file](#delete_file) - Delete a file.
* [delete_model](#delete_model) - Delete a fine-tuned model. You must have the Owner role in your organization.
* [download_file](#download_file) - Returns the contents of the specified file
* [~~list_engines~~](#list_engines) - Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability. :warning: **Deprecated**
* [list_files](#list_files) - Returns a list of files that belong to the user's organization.
* [list_fine_tune_events](#list_fine_tune_events) - Get fine-grained status updates for a fine-tune job.

* [list_fine_tunes](#list_fine_tunes) - List your organization's fine-tuning jobs

* [list_models](#list_models) - Lists the currently available models, and provides basic information about each one such as the owner and availability.
* [~~retrieve_engine~~](#retrieve_engine) - Retrieves a model instance, providing basic information about it such as the owner and availability. :warning: **Deprecated**
* [retrieve_file](#retrieve_file) - Returns information about a specific file.
* [retrieve_fine_tune](#retrieve_fine_tune) - Gets info about the fine-tune job.

[Learn more about Fine-tuning](/docs/guides/fine-tuning)

* [retrieve_model](#retrieve_model) - Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

## cancel_fine_tune

Immediately cancel a fine-tune job.


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.CancelFineTuneRequest(
    fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.open_ai.cancel_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CancelFineTuneRequest](../../models/operations/cancelfinetunerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CancelFineTuneResponse](../../models/operations/cancelfinetuneresponse.md)**


## ~~create_answer~~

Answers the specified question using the provided documents and examples.

The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions).


> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateAnswerRequest(
    documents=[
        'provident',
        'distinctio',
        'quibusdam',
    ],
    examples=[
        [
            'corrupti',
            'illum',
            'vel',
            'error',
        ],
        [
            'suscipit',
            'iure',
            'magnam',
        ],
        [
            'ipsa',
            'delectus',
            'tempora',
            'suscipit',
        ],
    ],
    examples_context='Ottawa, Canada's capital, is located in the east of southern Ontario, near the city of Montréal and the U.S. border.',
    expand=[
        'minus',
        'placeat',
    ],
    file='voluptatum',
    logit_bias='iusto',
    logprobs=568045,
    max_rerank=392785,
    max_tokens=925597,
    model='temporibus',
    n=71036,
    question='What is the capital of Japan?',
    return_metadata='quis',
    return_prompt=False,
    search_model='veritatis',
    stop=[
        '["\n"]',
    ],
    temperature=3682.41,
    user='repellendus',
)

res = s.open_ai.create_answer(req)

if res.create_answer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.CreateAnswerRequest](../../models/shared/createanswerrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateAnswerResponse](../../models/operations/createanswerresponse.md)**


## create_chat_completion

Creates a model response for the given chat conversation.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateChatCompletionRequest(
    frequency_penalty=9571.56,
    function_call=shared.CreateChatCompletionRequestFunctionCall2(
        name='Teri Strosin',
    ),
    functions=[
        shared.ChatCompletionFunctions(
            description='quod',
            name='Deanna Sauer MD',
            parameters={
                "occaecati": 'fugit',
                "deleniti": 'hic',
                "optio": 'totam',
            },
        ),
        shared.ChatCompletionFunctions(
            description='beatae',
            name='Tanya Gleason',
            parameters={
                "esse": 'ipsum',
                "excepturi": 'aspernatur',
                "perferendis": 'ad',
            },
        ),
        shared.ChatCompletionFunctions(
            description='natus',
            name='Sheryl Fadel',
            parameters={
                "saepe": 'fuga',
                "in": 'corporis',
                "iste": 'iure',
                "saepe": 'quidem',
            },
        ),
        shared.ChatCompletionFunctions(
            description='architecto',
            name='Lela Orn',
            parameters={
                "dolorem": 'corporis',
            },
        ),
    ],
    logit_bias=shared.CreateChatCompletionRequestLogitBias(),
    max_tokens=128926,
    messages=[
        shared.ChatCompletionRequestMessage(
            content='enim',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='omnis',
                name='Ms. Cathy Marks',
            ),
            name='Darrin Brakus',
            role=shared.ChatCompletionRequestMessageRole.ASSISTANT,
        ),
        shared.ChatCompletionRequestMessage(
            content='consequuntur',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='repellat',
                name='Tracy Fritsch',
            ),
            name='Shannon Mueller',
            role=shared.ChatCompletionRequestMessageRole.SYSTEM,
        ),
        shared.ChatCompletionRequestMessage(
            content='laborum',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='animi',
                name='Christina Satterfield',
            ),
            name='Mr. Alberta Schuster',
            role=shared.ChatCompletionRequestMessageRole.FUNCTION,
        ),
        shared.ChatCompletionRequestMessage(
            content='laborum',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='quasi',
                name='Jan Thiel',
            ),
            name='Jose Moen',
            role=shared.ChatCompletionRequestMessageRole.SYSTEM,
        ),
    ],
    model='doloremque',
    n=1,
    presence_penalty=4417.11,
    stop='maiores',
    stream=False,
    temperature=1,
    top_p=1,
    user='dicta',
)

res = s.open_ai.create_chat_completion(req)

if res.create_chat_completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateChatCompletionRequest](../../models/shared/createchatcompletionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateChatCompletionResponse](../../models/operations/createchatcompletionresponse.md)**


## ~~create_classification~~

Classifies the specified `query` using provided examples.

The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
to select the ones most relevant for the particular query. Then, the relevant examples
are combined with the query to construct a prompt to produce the final label via the
[completions](/docs/api-reference/completions) endpoint.

Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
request using the `examples` parameter for quick tests and small scale use cases.


> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateClassificationRequest(
    examples=[
        [
            'iusto',
            'dicta',
        ],
        [
            'enim',
            'accusamus',
            'commodi',
        ],
    ],
    expand='repudiandae',
    file='quae',
    labels=[
        'quidem',
    ],
    logit_bias='molestias',
    logprobs='excepturi',
    max_examples=865103,
    model='modi',
    query='The plot is not very attractive.',
    return_metadata='praesentium',
    return_prompt='rem',
    search_model='voluptates',
    temperature=0,
    user='quasi',
)

res = s.open_ai.create_classification(req)

if res.create_classification_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateClassificationRequest](../../models/shared/createclassificationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateClassificationResponse](../../models/operations/createclassificationresponse.md)**


## create_completion

Creates a completion for the provided prompt and parameters.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateCompletionRequest(
    best_of=921158,
    echo=False,
    frequency_penalty=5759.47,
    logit_bias=shared.CreateCompletionRequestLogitBias(),
    logprobs=83112,
    max_tokens=16,
    model='itaque',
    n=1,
    presence_penalty=2777.18,
    prompt=[
        'This is a test.',
    ],
    stop=[
        '["\n"]',
        '["\n"]',
        '["\n"]',
        '["\n"]',
    ],
    stream=False,
    suffix='test.',
    temperature=1,
    top_p=1,
    user='user-1234',
)

res = s.open_ai.create_completion(req)

if res.create_completion_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.CreateCompletionRequest](../../models/shared/createcompletionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateCompletionResponse](../../models/operations/createcompletionresponse.md)**


## create_edit

Creates a new edit for the provided input, instruction, and parameters.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateEditRequest(
    input='What day of the wek is it?',
    instruction='Fix the spelling mistakes.',
    model='explicabo',
    n=1,
    temperature=1,
    top_p=1,
)

res = s.open_ai.create_edit(req)

if res.create_edit_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateEditRequest](../../models/shared/createeditrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateEditResponse](../../models/operations/createeditresponse.md)**


## create_embedding

Creates an embedding vector representing the input text.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateEmbeddingRequest(
    input=[
        841386,
        289406,
        264730,
    ],
    model='qui',
    user='aliquid',
)

res = s.open_ai.create_embedding(req)

if res.create_embedding_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateEmbeddingRequest](../../models/shared/createembeddingrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateEmbeddingResponse](../../models/operations/createembeddingresponse.md)**


## create_file

Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.


### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateFileRequest(
    file=shared.CreateFileRequestFile(
        content='cupiditate'.encode(),
        file='quos',
    ),
    purpose='perferendis',
)

res = s.open_ai.create_file(req)

if res.open_ai_file is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateFileRequest](../../models/shared/createfilerequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateFileResponse](../../models/operations/createfileresponse.md)**


## create_fine_tune

Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about Fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateFineTuneRequest(
    batch_size=164940,
    classification_betas=[
        3698.08,
        46.95,
        1464.41,
        6778.17,
    ],
    classification_n_classes=569618,
    classification_positive_class='tempora',
    compute_classification_metrics=False,
    learning_rate_multiplier=7037.37,
    model='tempore',
    n_epochs=288476,
    prompt_loss_weight=9621.89,
    suffix='eum',
    training_file='file-ajSREls59WBbvgSzJSVWxMCB',
    validation_file='file-XjSREls59WBbvgSzJSVWxMCa',
)

res = s.open_ai.create_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CreateFineTuneRequest](../../models/shared/createfinetunerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateFineTuneResponse](../../models/operations/createfinetuneresponse.md)**


## create_image

Creates an image given a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateImageRequest(
    n=1,
    prompt='A cute baby sea otter',
    response_format=shared.CreateImageRequestResponseFormat.URL,
    size=shared.CreateImageRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='non',
)

res = s.open_ai.create_image(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CreateImageRequest](../../models/shared/createimagerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateImageResponse](../../models/operations/createimageresponse.md)**


## create_image_edit

Creates an edited or extended image given an original image and a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateImageEditRequest(
    image=shared.CreateImageEditRequestImage(
        content='eligendi'.encode(),
        image='sint',
    ),
    mask=shared.CreateImageEditRequestMask(
        content='aliquid'.encode(),
        mask='provident',
    ),
    n='necessitatibus',
    prompt='A cute baby sea otter wearing a beret',
    response_format='sint',
    size='officia',
    user='dolor',
)

res = s.open_ai.create_image_edit(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateImageEditRequest](../../models/shared/createimageeditrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateImageEditResponse](../../models/operations/createimageeditresponse.md)**


## create_image_variation

Creates a variation of a given image.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateImageVariationRequest(
    image=shared.CreateImageVariationRequestImage(
        content='debitis'.encode(),
        image='a',
    ),
    n='dolorum',
    response_format='in',
    size='in',
    user='illum',
)

res = s.open_ai.create_image_variation(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateImageVariationRequest](../../models/shared/createimagevariationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateImageVariationResponse](../../models/operations/createimagevariationresponse.md)**


## create_moderation

Classifies if text violates OpenAI's Content Policy

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateModerationRequest(
    input=[
        'I want to kill them.',
        'I want to kill them.',
        'I want to kill them.',
    ],
    model='text-moderation-stable',
)

res = s.open_ai.create_moderation(req)

if res.create_moderation_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.CreateModerationRequest](../../models/shared/createmoderationrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateModerationResponse](../../models/operations/createmoderationresponse.md)**


## ~~create_search~~

The search endpoint computes similarity scores between provided query and documents. Documents can be passed directly to the API if there are no more than 200 of them.

To go beyond the 200 document limit, documents can be processed offline and then used for efficient retrieval at query time. When `file` is set, the search endpoint searches over all the documents in the given file and returns up to the `max_rerank` number of documents. These documents will be returned along with their search scores.

The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go higher), where a score above 200 usually means the document is semantically similar to the query.


> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt()

req = operations.CreateSearchRequest(
    create_search_request=shared.CreateSearchRequest(
        documents=[
            'magnam',
        ],
        file='cumque',
        max_rerank=813798,
        query='the president',
        return_metadata=False,
        user='ea',
    ),
    engine_id='davinci',
)

res = s.open_ai.create_search(req)

if res.create_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateSearchRequest](../../models/operations/createsearchrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateSearchResponse](../../models/operations/createsearchresponse.md)**


## create_transcription

Transcribes audio into the input language.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateTranscriptionRequest(
    file=shared.CreateTranscriptionRequestFile(
        content='aliquid'.encode(),
        file='laborum',
    ),
    language='accusamus',
    model='non',
    prompt='occaecati',
    response_format='enim',
    temperature=8817.36,
)

res = s.open_ai.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.CreateTranscriptionRequest](../../models/shared/createtranscriptionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateTranscriptionResponse](../../models/operations/createtranscriptionresponse.md)**


## create_translation

Translates audio into into English.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateTranslationRequest(
    file=shared.CreateTranslationRequestFile(
        content='delectus'.encode(),
        file='quidem',
    ),
    model='provident',
    prompt='nam',
    response_format='id',
    temperature=5013.24,
)

res = s.open_ai.create_translation(req)

if res.create_translation_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.CreateTranslationRequest](../../models/shared/createtranslationrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateTranslationResponse](../../models/operations/createtranslationresponse.md)**


## delete_file

Delete a file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.DeleteFileRequest(
    file_id='deleniti',
)

res = s.open_ai.delete_file(req)

if res.delete_file_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteFileRequest](../../models/operations/deletefilerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**


## delete_model

Delete a fine-tuned model. You must have the Owner role in your organization.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.DeleteModelRequest(
    model='curie:ft-acmeco-2021-03-03-21-44-20',
)

res = s.open_ai.delete_model(req)

if res.delete_model_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.DeleteModelRequest](../../models/operations/deletemodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteModelResponse](../../models/operations/deletemodelresponse.md)**


## download_file

Returns the contents of the specified file

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.DownloadFileRequest(
    file_id='sapiente',
)

res = s.open_ai.download_file(req)

if res.download_file_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DownloadFileRequest](../../models/operations/downloadfilerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DownloadFileResponse](../../models/operations/downloadfileresponse.md)**


## ~~list_engines~~

Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt


s = gpt.Gpt()


res = s.open_ai.list_engines()

if res.list_engines_response is not None:
    # handle response
```


### Response

**[operations.ListEnginesResponse](../../models/operations/listenginesresponse.md)**


## list_files

Returns a list of files that belong to the user's organization.

### Example Usage

```python
import gpt


s = gpt.Gpt()


res = s.open_ai.list_files()

if res.list_files_response is not None:
    # handle response
```


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**


## list_fine_tune_events

Get fine-grained status updates for a fine-tune job.


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.ListFineTuneEventsRequest(
    fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
    stream=False,
)

res = s.open_ai.list_fine_tune_events(req)

if res.list_fine_tune_events_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListFineTuneEventsRequest](../../models/operations/listfinetuneeventsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListFineTuneEventsResponse](../../models/operations/listfinetuneeventsresponse.md)**


## list_fine_tunes

List your organization's fine-tuning jobs


### Example Usage

```python
import gpt


s = gpt.Gpt()


res = s.open_ai.list_fine_tunes()

if res.list_fine_tunes_response is not None:
    # handle response
```


### Response

**[operations.ListFineTunesResponse](../../models/operations/listfinetunesresponse.md)**


## list_models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Example Usage

```python
import gpt


s = gpt.Gpt()


res = s.open_ai.list_models()

if res.list_models_response is not None:
    # handle response
```


### Response

**[operations.ListModelsResponse](../../models/operations/listmodelsresponse.md)**


## ~~retrieve_engine~~

Retrieves a model instance, providing basic information about it such as the owner and availability.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveEngineRequest(
    engine_id='davinci',
)

res = s.open_ai.retrieve_engine(req)

if res.engine is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RetrieveEngineRequest](../../models/operations/retrieveenginerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.RetrieveEngineResponse](../../models/operations/retrieveengineresponse.md)**


## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveFileRequest(
    file_id='amet',
)

res = s.open_ai.retrieve_file(req)

if res.open_ai_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RetrieveFileRequest](../../models/operations/retrievefilerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.RetrieveFileResponse](../../models/operations/retrievefileresponse.md)**


## retrieve_fine_tune

Gets info about the fine-tune job.

[Learn more about Fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveFineTuneRequest(
    fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.open_ai.retrieve_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RetrieveFineTuneRequest](../../models/operations/retrievefinetunerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RetrieveFineTuneResponse](../../models/operations/retrievefinetuneresponse.md)**


## retrieve_model

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveModelRequest(
    model='text-davinci-001',
)

res = s.open_ai.retrieve_model(req)

if res.model is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RetrieveModelRequest](../../models/operations/retrievemodelrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RetrieveModelResponse](../../models/operations/retrievemodelresponse.md)**

