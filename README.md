# OpenAPI Python SDK

![OpenAI_Logo_Black](https://user-images.githubusercontent.com/6267663/220744241-48f469af-40b6-4d7f-ab48-8426b30189f0.svg#gh-light-mode-only)
![OpenAI_Logo_White](https://user-images.githubusercontent.com/6267663/220744513-66c99d0e-ed91-4577-982f-e7128d35ce95.svg#gh-dark-mode-only)

<div align="center">
   <p><strong>This is an unofficial SDK for the OpenAI API.</strong> The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or code. We offer a spectrum of models with different levels of power suitable for different tasks, as well as the ability to fine-tune your own custom models. These models can be used for everything from content generation to semantic search and classification.</p>
   <a href="https://github.com/speakeasy-sdks/openai-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/openai-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://platform.openai.com/docs/introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=2ca47c&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install openai-python
```
<!-- End SDK Installation -->

## Authentication

The OpenAI API uses API keys for authentication. Visit your API Keys page to retrieve the API key you'll use in your requests.

**Remember that your API key is a secret!** Do not share it with others or expose it in any client-side code (browsers, apps). Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an Authorization HTTP header as follows:

```bash
Authorization: Bearer YOUR_API_KEY
```

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateTranscriptionRequest(
    file=shared.CreateTranscriptionRequestFile(
        content='\#BbTW\'zX9'.encode(),
        file='string',
    ),
shared.CreateTranscriptionRequestModel2.WHISPER_1,
)

res = s.audio.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [audio](docs/sdks/audio/README.md)

* [create_transcription](docs/sdks/audio/README.md#create_transcription) - Transcribes audio into the input language.
* [create_translation](docs/sdks/audio/README.md#create_translation) - Translates audio into English.

### [chat](docs/sdks/chat/README.md)

* [create_chat_completion](docs/sdks/chat/README.md#create_chat_completion) - Creates a model response for the given chat conversation.

### [completions](docs/sdks/completions/README.md)

* [create_completion](docs/sdks/completions/README.md#create_completion) - Creates a completion for the provided prompt and parameters.

### [edits](docs/sdks/edits/README.md)

* [~~create_edit~~](docs/sdks/edits/README.md#create_edit) - Creates a new edit for the provided input, instruction, and parameters. :warning: **Deprecated**

### [embeddings](docs/sdks/embeddings/README.md)

* [create_embedding](docs/sdks/embeddings/README.md#create_embedding) - Creates an embedding vector representing the input text.

### [files](docs/sdks/files/README.md)

* [create_file](docs/sdks/files/README.md#create_file) - Upload a file that can be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please [contact us](https://help.openai.com/) if you need to increase the storage limit.

* [delete_file](docs/sdks/files/README.md#delete_file) - Delete a file.
* [download_file](docs/sdks/files/README.md#download_file) - Returns the contents of the specified file.
* [list_files](docs/sdks/files/README.md#list_files) - Returns a list of files that belong to the user's organization.
* [retrieve_file](docs/sdks/files/README.md#retrieve_file) - Returns information about a specific file.

### [fine_tunes](docs/sdks/finetunes/README.md)

* [~~cancel_fine_tune~~](docs/sdks/finetunes/README.md#cancel_fine_tune) - Immediately cancel a fine-tune job.
 :warning: **Deprecated**
* [~~create_fine_tune~~](docs/sdks/finetunes/README.md#create_fine_tune) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**
* [~~list_fine_tune_events~~](docs/sdks/finetunes/README.md#list_fine_tune_events) - Get fine-grained status updates for a fine-tune job.
 :warning: **Deprecated**
* [~~list_fine_tunes~~](docs/sdks/finetunes/README.md#list_fine_tunes) - List your organization's fine-tuning jobs
 :warning: **Deprecated**
* [~~retrieve_fine_tune~~](docs/sdks/finetunes/README.md#retrieve_fine_tune) - Gets info about the fine-tune job.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**

### [fine_tuning](docs/sdks/finetuning/README.md)

* [cancel_fine_tuning_job](docs/sdks/finetuning/README.md#cancel_fine_tuning_job) - Immediately cancel a fine-tune job.

* [create_fine_tuning_job](docs/sdks/finetuning/README.md#create_fine_tuning_job) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

* [list_fine_tuning_events](docs/sdks/finetuning/README.md#list_fine_tuning_events) - Get status updates for a fine-tuning job.

* [list_paginated_fine_tuning_jobs](docs/sdks/finetuning/README.md#list_paginated_fine_tuning_jobs) - List your organization's fine-tuning jobs

* [retrieve_fine_tuning_job](docs/sdks/finetuning/README.md#retrieve_fine_tuning_job) - Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


### [images](docs/sdks/images/README.md)

* [create_image](docs/sdks/images/README.md#create_image) - Creates an image given a prompt.
* [create_image_edit](docs/sdks/images/README.md#create_image_edit) - Creates an edited or extended image given an original image and a prompt.
* [create_image_variation](docs/sdks/images/README.md#create_image_variation) - Creates a variation of a given image.

### [models](docs/sdks/models/README.md)

* [delete_model](docs/sdks/models/README.md#delete_model) - Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
* [list_models](docs/sdks/models/README.md#list_models) - Lists the currently available models, and provides basic information about each one such as the owner and availability.
* [retrieve_model](docs/sdks/models/README.md#retrieve_model) - Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### [moderations](docs/sdks/moderations/README.md)

* [create_moderation](docs/sdks/moderations/README.md#create_moderation) - Classifies if text violates OpenAI's Content Policy
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
