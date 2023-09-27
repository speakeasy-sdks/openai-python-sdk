# OpenAI
(*open_ai*)

## Overview

The OpenAI REST API

### Available Operations

* [~~cancel_fine_tune~~](#cancel_fine_tune) - Immediately cancel a fine-tune job.
 :warning: **Deprecated**
* [cancel_fine_tuning_job](#cancel_fine_tuning_job) - Immediately cancel a fine-tune job.

* [create_chat_completion](#create_chat_completion) - Creates a model response for the given chat conversation.
* [create_completion](#create_completion) - Creates a completion for the provided prompt and parameters.
* [~~create_edit~~](#create_edit) - Creates a new edit for the provided input, instruction, and parameters. :warning: **Deprecated**
* [create_embedding](#create_embedding) - Creates an embedding vector representing the input text.
* [create_file](#create_file) - Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.

* [~~create_fine_tune~~](#create_fine_tune) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**
* [create_fine_tuning_job](#create_fine_tuning_job) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

* [create_image](#create_image) - Creates an image given a prompt.
* [create_image_edit](#create_image_edit) - Creates an edited or extended image given an original image and a prompt.
* [create_image_variation](#create_image_variation) - Creates a variation of a given image.
* [create_moderation](#create_moderation) - Classifies if text violates OpenAI's Content Policy
* [create_transcription](#create_transcription) - Transcribes audio into the input language.
* [create_translation](#create_translation) - Translates audio into English.
* [delete_file](#delete_file) - Delete a file.
* [delete_model](#delete_model) - Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
* [download_file](#download_file) - Returns the contents of the specified file.
* [list_files](#list_files) - Returns a list of files that belong to the user's organization.
* [~~list_fine_tune_events~~](#list_fine_tune_events) - Get fine-grained status updates for a fine-tune job.
 :warning: **Deprecated**
* [~~list_fine_tunes~~](#list_fine_tunes) - List your organization's fine-tuning jobs
 :warning: **Deprecated**
* [list_fine_tuning_events](#list_fine_tuning_events) - Get status updates for a fine-tuning job.

* [list_models](#list_models) - Lists the currently available models, and provides basic information about each one such as the owner and availability.
* [list_paginated_fine_tuning_jobs](#list_paginated_fine_tuning_jobs) - List your organization's fine-tuning jobs

* [retrieve_file](#retrieve_file) - Returns information about a specific file.
* [~~retrieve_fine_tune~~](#retrieve_fine_tune) - Gets info about the fine-tune job.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**
* [retrieve_fine_tuning_job](#retrieve_fine_tuning_job) - Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

* [retrieve_model](#retrieve_model) - Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

## ~~cancel_fine_tune~~

Immediately cancel a fine-tune job.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

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


## cancel_fine_tuning_job

Immediately cancel a fine-tune job.


### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CancelFineTuningJobRequest(
    fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.open_ai.cancel_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CancelFineTuningJobRequest](../../models/operations/cancelfinetuningjobrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CancelFineTuningJobResponse](../../models/operations/cancelfinetuningjobresponse.md)**


## create_chat_completion

Creates a model response for the given chat conversation.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateChatCompletionRequest(
    frequency_penalty=5488.14,
    function_call=[],
    functions=[
        shared.ChatCompletionFunctions(
            description='provident',
            name='Ellis Mitchell',
            parameters={
                "illum": 'vel',
            },
        ),
    ],
    logit_bias={
        "error": 645894,
    },
    max_tokens=384382,
    messages=[
        shared.ChatCompletionRequestMessage(
            content='iure',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='magnam',
                name='Larry Windler',
            ),
            name='Alexandra Schulist',
            role=shared.ChatCompletionRequestMessageRole.ASSISTANT,
        ),
    ],
    model=[],
    n=1,
    presence_penalty=3927.85,
    stop=[],
    stream=False,
    temperature=1,
    top_p=1,
    user='user-1234',
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
    best_of=925597,
    echo=False,
    frequency_penalty=8360.79,
    logit_bias={
        "ab": 337396,
    },
    logprobs=87129,
    max_tokens=16,
    model=[],
    n=1,
    presence_penalty=6481.72,
    prompt=[],
    stop=[],
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
    model=[],
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

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateEmbeddingRequest(
    input=[],
    model=[],
    user='user-1234',
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

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateFileRequest(
    file=shared.CreateFileRequestFile(
        content='perferendis'.encode(),
        file='ipsam',
    ),
    purpose='repellendus',
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


## ~~create_fine_tune~~

Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)


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

req = shared.CreateFineTuneRequest(
    batch_size=957156,
    classification_betas=[
        7781.57,
    ],
    classification_n_classes=140350,
    classification_positive_class='at',
    compute_classification_metrics=False,
    learning_rate_multiplier=8700.88,
    model=[],
    n_epochs=978619,
    prompt_loss_weight=4736.08,
    suffix='quod',
    training_file='file-abc123',
    validation_file='file-abc123',
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


## create_fine_tuning_job

Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateFineTuningJobRequest(
    hyperparameters=shared.CreateFineTuningJobRequestHyperparameters(
        n_epochs=[],
    ),
    model=[],
    suffix='quod',
    training_file='file-abc123',
    validation_file='file-abc123',
)

res = s.open_ai.create_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.CreateFineTuningJobRequest](../../models/shared/createfinetuningjobrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateFineTuningJobResponse](../../models/operations/createfinetuningjobresponse.md)**


## create_image

Creates an image given a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageRequest(
    n=1,
    prompt='A cute baby sea otter',
    response_format=shared.CreateImageRequestResponseFormat.URL,
    size=shared.CreateImageRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
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

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageEditRequest2(
    image=shared.CreateImageEditRequestImage(
        content='esse'.encode(),
        image='totam',
    ),
    mask=shared.CreateImageEditRequestMask(
        content='porro'.encode(),
        mask='dolorum',
    ),
    n=1,
    prompt='A cute baby sea otter wearing a beret',
    response_format=shared.CreateImageEditRequestResponseFormat.URL,
    size=shared.CreateImageEditRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.open_ai.create_image_edit(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.CreateImageEditRequest2](../../models/shared/createimageeditrequest2.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateImageEditResponse](../../models/operations/createimageeditresponse.md)**


## create_image_variation

Creates a variation of a given image.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageVariationRequest2(
    image=shared.CreateImageVariationRequestImage(
        content='dicta'.encode(),
        image='nam',
    ),
    n=1,
    response_format=shared.CreateImageVariationRequestResponseFormat.URL,
    size=shared.CreateImageVariationRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.open_ai.create_image_variation(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.CreateImageVariationRequest2](../../models/shared/createimagevariationrequest2.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateImageVariationResponse](../../models/operations/createimagevariationresponse.md)**


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
    input=[],
    model=[],
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


## create_transcription

Transcribes audio into the input language.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateTranscriptionRequest3(
    file=shared.CreateTranscriptionRequestFile(
        content='officia'.encode(),
        file='occaecati',
    ),
    language='fugit',
    model=[],
    prompt='deleniti',
    response_format=shared.CreateTranscriptionRequestResponseFormat.VTT,
    temperature=7586.16,
)

res = s.open_ai.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateTranscriptionRequest3](../../models/shared/createtranscriptionrequest3.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateTranscriptionResponse](../../models/operations/createtranscriptionresponse.md)**


## create_translation

Translates audio into English.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateTranslationRequest1(
    file=shared.CreateTranslationRequestFile(
        content='totam'.encode(),
        file='beatae',
    ),
    model=[],
    prompt='commodi',
    response_format='molestiae',
    temperature=2645.55,
)

res = s.open_ai.create_translation(req)

if res.create_translation_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.CreateTranslationRequest1](../../models/shared/createtranslationrequest1.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateTranslationResponse](../../models/operations/createtranslationresponse.md)**


## delete_file

Delete a file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.DeleteFileRequest(
    file_id='qui',
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

Returns the contents of the specified file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.DownloadFileRequest(
    file_id='impedit',
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


## list_files

Returns a list of files that belong to the user's organization.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.open_ai.list_files()

if res.list_files_response is not None:
    # handle response
```


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**


## ~~list_fine_tune_events~~

Get fine-grained status updates for a fine-tune job.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

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


## ~~list_fine_tunes~~

List your organization's fine-tuning jobs


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


res = s.open_ai.list_fine_tunes()

if res.list_fine_tunes_response is not None:
    # handle response
```


### Response

**[operations.ListFineTunesResponse](../../models/operations/listfinetunesresponse.md)**


## list_fine_tuning_events

Get status updates for a fine-tuning job.


### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.ListFineTuningEventsRequest(
    after='cum',
    fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
    limit=456150,
)

res = s.open_ai.list_fine_tuning_events(req)

if res.list_fine_tuning_job_events_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListFineTuningEventsRequest](../../models/operations/listfinetuningeventsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ListFineTuningEventsResponse](../../models/operations/listfinetuningeventsresponse.md)**


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


res = s.open_ai.list_models()

if res.list_models_response is not None:
    # handle response
```


### Response

**[operations.ListModelsResponse](../../models/operations/listmodelsresponse.md)**


## list_paginated_fine_tuning_jobs

List your organization's fine-tuning jobs


### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.ListPaginatedFineTuningJobsRequest(
    after='ipsum',
    limit=568434,
)

res = s.open_ai.list_paginated_fine_tuning_jobs(req)

if res.list_paginated_fine_tuning_jobs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListPaginatedFineTuningJobsRequest](../../models/operations/listpaginatedfinetuningjobsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ListPaginatedFineTuningJobsResponse](../../models/operations/listpaginatedfinetuningjobsresponse.md)**


## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.RetrieveFileRequest(
    file_id='aspernatur',
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


## ~~retrieve_fine_tune~~

Gets info about the fine-tune job.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

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


## retrieve_fine_tuning_job

Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.RetrieveFineTuningJobRequest(
    fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.open_ai.retrieve_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RetrieveFineTuningJobRequest](../../models/operations/retrievefinetuningjobrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RetrieveFineTuningJobResponse](../../models/operations/retrievefinetuningjobresponse.md)**


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

