# open_ai

## Overview

The OpenAI REST API

### Available Operations

* [cancel_fine_tune](#cancel_fine_tune) - Immediately cancel a fine-tune job.

* [create_chat_completion](#create_chat_completion) - Creates a model response for the given chat conversation.
* [create_completion](#create_completion) - Creates a completion for the provided prompt and parameters.
* [~~create_edit~~](#create_edit) - Creates a new edit for the provided input, instruction, and parameters. :warning: **Deprecated**
* [create_embedding](#create_embedding) - Creates an embedding vector representing the input text.
* [create_file](#create_file) - Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.

* [create_fine_tune](#create_fine_tune) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about Fine-tuning](/docs/guides/fine-tuning)

* [create_image](#create_image) - Creates an image given a prompt.
* [create_image_edit](#create_image_edit) - Creates an edited or extended image given an original image and a prompt.
* [create_image_variation](#create_image_variation) - Creates a variation of a given image.
* [create_moderation](#create_moderation) - Classifies if text violates OpenAI's Content Policy
* [create_transcription](#create_transcription) - Transcribes audio into the input language.
* [create_translation](#create_translation) - Translates audio into English.
* [delete_file](#delete_file) - Delete a file.
* [delete_model](#delete_model) - Delete a fine-tuned model. You must have the Owner role in your organization.
* [download_file](#download_file) - Returns the contents of the specified file
* [list_files](#list_files) - Returns a list of files that belong to the user's organization.
* [list_fine_tune_events](#list_fine_tune_events) - Get fine-grained status updates for a fine-tune job.

* [list_fine_tunes](#list_fine_tunes) - List your organization's fine-tuning jobs

* [list_models](#list_models) - Lists the currently available models, and provides basic information about each one such as the owner and availability.
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


## create_chat_completion

Creates a model response for the given chat conversation.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateChatCompletionRequest(
    frequency_penalty=5488.14,
    function_call=shared.CreateChatCompletionRequestFunctionCall2(
        name='Ellis Mitchell',
    ),
    functions=[
        shared.ChatCompletionFunctions(
            description='vel',
            name='Doug Hoppe',
            parameters={
                "ipsa": 'delectus',
                "tempora": 'suscipit',
                "molestiae": 'minus',
                "placeat": 'voluptatum',
            },
        ),
        shared.ChatCompletionFunctions(
            description='iusto',
            name='Charlie Walsh II',
            parameters={
                "deserunt": 'perferendis',
            },
        ),
        shared.ChatCompletionFunctions(
            description='ipsam',
            name='Timmy Satterfield',
            parameters={
                "maiores": 'molestiae',
                "quod": 'quod',
                "esse": 'totam',
                "porro": 'dolorum',
            },
        ),
        shared.ChatCompletionFunctions(
            description='dicta',
            name='Luke McCullough',
            parameters={
                "optio": 'totam',
                "beatae": 'commodi',
                "molestiae": 'modi',
                "qui": 'impedit',
            },
        ),
    ],
    logit_bias={
        "esse": 216550,
        "excepturi": 135218,
        "perferendis": 324141,
    },
    max_tokens=617636,
    messages=[
        shared.ChatCompletionRequestMessage(
            content='iste',
            function_call=shared.ChatCompletionRequestMessageFunctionCall(
                arguments='dolor',
                name='Lester Welch',
            ),
            name='Stacy Moore',
            role=shared.ChatCompletionRequestMessageRole.ASSISTANT,
        ),
    ],
    model='gpt-3.5-turbo',
    n=1,
    presence_penalty=602.25,
    stop=[
        'mollitia',
        'laborum',
        'dolores',
    ],
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

s = gpt.Gpt()

req = shared.CreateCompletionRequest(
    best_of=210382,
    echo=False,
    frequency_penalty=3581.52,
    logit_bias={
        "nobis": 315428,
    },
    logprobs=607831,
    max_tokens=16,
    model='minima',
    n=1,
    presence_penalty=5701.97,
    prompt='This is a test.',
    stop='
',
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

s = gpt.Gpt()

req = shared.CreateEditRequest(
    input='What day of the wek is it?',
    instruction='Fix the spelling mistakes.',
    model=shared.CreateEditRequestModel2.TEXT_DAVINCI_EDIT_001,
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
        [
            652790,
        ],
        [
            635059,
        ],
        [
            995300,
        ],
        [
            581850,
            253291,
            414369,
        ],
    ],
    model='text-embedding-ada-002',
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

s = gpt.Gpt()

req = shared.CreateFileRequest(
    file=shared.CreateFileRequestFile(
        content='molestiae'.encode(),
        file='velit',
    ),
    purpose='error',
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
    batch_size=158969,
    classification_betas=[
        1103.75,
        6747.52,
    ],
    classification_n_classes=656330,
    classification_positive_class='enim',
    compute_classification_metrics=False,
    learning_rate_multiplier=1381.83,
    model=shared.CreateFineTuneRequestModel2.CURIE,
    n_epochs=196582,
    prompt_loss_weight=9495.72,
    suffix='ipsam',
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

s = gpt.Gpt()

req = shared.CreateImageEditRequest2(
    image=shared.CreateImageEditRequestImage(
        content='id'.encode(),
        image='possimus',
    ),
    mask=shared.CreateImageEditRequestMask(
        content='aut'.encode(),
        mask='quasi',
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

s = gpt.Gpt()

req = shared.CreateImageVariationRequest2(
    image=shared.CreateImageVariationRequestImage(
        content='error'.encode(),
        image='temporibus',
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

s = gpt.Gpt()

req = shared.CreateModerationRequest(
    input=[
        'I want to kill them.',
    ],
    model=shared.CreateModerationRequestModel2.TEXT_MODERATION_STABLE,
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

s = gpt.Gpt()

req = shared.CreateTranscriptionRequest1(
    file=shared.CreateTranscriptionRequestFile(
        content='voluptatibus'.encode(),
        file='vero',
    ),
    language='nihil',
    model=shared.CreateTranscriptionRequestModel2.WHISPER_1,
    prompt='voluptatibus',
    response_format=shared.CreateTranscriptionRequestResponseFormat.JSON,
    temperature=6048.46,
)

res = s.open_ai.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateTranscriptionRequest1](../../models/shared/createtranscriptionrequest1.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateTranscriptionResponse](../../models/operations/createtranscriptionresponse.md)**


## create_translation

Translates audio into English.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateTranslationRequest(
    file=shared.CreateTranslationRequestFile(
        content='voluptate'.encode(),
        file='cum',
    ),
    model='whisper-1',
    prompt='doloremque',
    response_format='reprehenderit',
    temperature=2828.07,
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
    file_id='maiores',
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
    file_id='dicta',
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


## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveFileRequest(
    file_id='corporis',
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

