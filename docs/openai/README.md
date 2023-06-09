# open_ai

## Overview

The OpenAI REST API

### Available Operations

* [cancel_fine_tune](#cancel_fine_tune) - Immediately cancel a fine-tune job.

* [~~create_answer~~](#create_answer) - Answers the specified question using the provided documents and examples.

The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions).
 :warning: **Deprecated**
* [create_chat_completion](#create_chat_completion) - Creates a completion for the chat message
* [~~create_classification~~](#create_classification) - Classifies the specified `query` using provided examples.

The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
to select the ones most relevant for the particular query. Then, the relevant examples
are combined with the query to construct a prompt to produce the final label via the
[completions](/docs/api-reference/completions) endpoint.

Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
request using the `examples` parameter for quick tests and small scale use cases.
 :warning: **Deprecated**
* [create_completion](#create_completion) - Creates a completion for the provided prompt and parameters
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

## create_chat_completion

Creates a completion for the chat message

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateChatCompletionRequest(
    frequency_penalty=9571.56,
    logit_bias={
        "odit": 'at',
        "at": 'maiores',
        "molestiae": 'quod',
        "quod": 'esse',
    },
    max_tokens=520478,
    messages=[
        shared.ChatCompletionRequestMessage(
            content='dolorum',
            name='Antoinette Nikolaus',
            role=shared.ChatCompletionRequestMessageRole.USER,
        ),
        shared.ChatCompletionRequestMessage(
            content='hic',
            name='Everett Breitenberg',
            role=shared.ChatCompletionRequestMessageRole.SYSTEM,
        ),
        shared.ChatCompletionRequestMessage(
            content='qui',
            name='Jonathon Klocko',
            role=shared.ChatCompletionRequestMessageRole.SYSTEM,
        ),
        shared.ChatCompletionRequestMessage(
            content='perferendis',
            name='Faye Cormier',
            role=shared.ChatCompletionRequestMessageRole.USER,
        ),
    ],
    model='laboriosam',
    n=1,
    presence_penalty=9437.49,
    stop=[
        'in',
        'corporis',
        'iste',
    ],
    stream=False,
    temperature=1,
    top_p=1,
    user='iure',
)

res = s.open_ai.create_chat_completion(req)

if res.create_chat_completion_response is not None:
    # handle response
```

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
            'architecto',
            'ipsa',
            'reiciendis',
        ],
        [
            'mollitia',
            'laborum',
            'dolores',
        ],
        [
            'corporis',
        ],
        [
            'nobis',
        ],
    ],
    expand='enim',
    file='omnis',
    labels=[
        'minima',
        'excepturi',
    ],
    logit_bias='accusantium',
    logprobs='iure',
    max_examples=634274,
    model='doloribus',
    query='The plot is not very attractive.',
    return_metadata='sapiente',
    return_prompt='architecto',
    search_model='mollitia',
    temperature=0,
    user='dolorem',
)

res = s.open_ai.create_classification(req)

if res.create_classification_response is not None:
    # handle response
```

## create_completion

Creates a completion for the provided prompt and parameters

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateCompletionRequest(
    best_of=635059,
    echo=False,
    frequency_penalty=1613.09,
    logit_bias={
        "mollitia": 'occaecati',
        "numquam": 'commodi',
        "quam": 'molestiae',
        "velit": 'error',
    },
    logprobs=158969,
    max_tokens=16,
    model='quis',
    n=1,
    presence_penalty=1103.75,
    prompt=[
        317202,
        138183,
        778346,
    ],
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
    model='tenetur',
    n=1,
    temperature=1,
    top_p=1,
)

res = s.open_ai.create_edit(req)

if res.create_edit_response is not None:
    # handle response
```

## create_embedding

Creates an embedding vector representing the input text.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateEmbeddingRequest(
    input=[
        'This is a test.',
        'This is a test.',
        'This is a test.',
    ],
    model='possimus',
    user='aut',
)

res = s.open_ai.create_embedding(req)

if res.create_embedding_response is not None:
    # handle response
```

## create_file

Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.


### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateFileRequest(
    file=shared.CreateFileRequestFile(
        content='quasi'.encode(),
        file='error',
    ),
    purpose='temporibus',
)

res = s.open_ai.create_file(req)

if res.open_ai_file is not None:
    # handle response
```

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
    batch_size=673660,
    classification_betas=[
        9719.45,
    ],
    classification_n_classes=976460,
    classification_positive_class='vero',
    compute_classification_metrics=False,
    learning_rate_multiplier=4686.51,
    model='praesentium',
    n_epochs=976762,
    prompt_loss_weight=557.14,
    suffix='omnis',
    training_file='file-ajSREls59WBbvgSzJSVWxMCB',
    validation_file='file-XjSREls59WBbvgSzJSVWxMCa',
)

res = s.open_ai.create_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```

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
    user='voluptate',
)

res = s.open_ai.create_image(req)

if res.images_response is not None:
    # handle response
```

## create_image_edit

Creates an edited or extended image given an original image and a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateImageEditRequest(
    image=shared.CreateImageEditRequestImage(
        content='cum'.encode(),
        image='perferendis',
    ),
    mask=shared.CreateImageEditRequestMask(
        content='doloremque'.encode(),
        mask='reprehenderit',
    ),
    n='ut',
    prompt='A cute baby sea otter wearing a beret',
    response_format='maiores',
    size='dicta',
    user='corporis',
)

res = s.open_ai.create_image_edit(req)

if res.images_response is not None:
    # handle response
```

## create_image_variation

Creates a variation of a given image.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateImageVariationRequest(
    image=shared.CreateImageVariationRequestImage(
        content='dolore'.encode(),
        image='iusto',
    ),
    n='dicta',
    response_format='harum',
    size='enim',
    user='accusamus',
)

res = s.open_ai.create_image_variation(req)

if res.images_response is not None:
    # handle response
```

## create_moderation

Classifies if text violates OpenAI's Content Policy

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateModerationRequest(
    input='I want to kill them.',
    model='text-moderation-stable',
)

res = s.open_ai.create_moderation(req)

if res.create_moderation_response is not None:
    # handle response
```

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
            'quae',
            'ipsum',
            'quidem',
            'molestias',
        ],
        file='excepturi',
        max_rerank=865103,
        query='the president',
        return_metadata=False,
        user='modi',
    ),
    engine_id='davinci',
)

res = s.open_ai.create_search(req)

if res.create_search_response is not None:
    # handle response
```

## create_transcription

Transcribes audio into the input language.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateTranscriptionRequest(
    file=shared.CreateTranscriptionRequestFile(
        content='praesentium'.encode(),
        file='rem',
    ),
    language='voluptates',
    model='quasi',
    prompt='repudiandae',
    response_format='sint',
    temperature=831.12,
)

res = s.open_ai.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
```

## create_translation

Translates audio into into English.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt()

req = shared.CreateTranslationRequest(
    file=shared.CreateTranslationRequestFile(
        content='itaque'.encode(),
        file='incidunt',
    ),
    model='enim',
    prompt='consequatur',
    response_format='est',
    temperature=8423.42,
)

res = s.open_ai.create_translation(req)

if res.create_translation_response is not None:
    # handle response
```

## delete_file

Delete a file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.DeleteFileRequest(
    file_id='explicabo',
)

res = s.open_ai.delete_file(req)

if res.delete_file_response is not None:
    # handle response
```

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

## download_file

Returns the contents of the specified file

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.DownloadFileRequest(
    file_id='deserunt',
)

res = s.open_ai.download_file(req)

if res.download_file_200_application_json_string is not None:
    # handle response
```

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

## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt()

req = operations.RetrieveFileRequest(
    file_id='distinctio',
)

res = s.open_ai.retrieve_file(req)

if res.open_ai_file is not None:
    # handle response
```

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
