# OpenAPI Python SDK

![OpenAI_Logo_Black](https://user-images.githubusercontent.com/6267663/220744241-48f469af-40b6-4d7f-ab48-8426b30189f0.svg#gh-light-mode-only)
![OpenAI_Logo_White](https://user-images.githubusercontent.com/6267663/220744513-66c99d0e-ed91-4577-982f-e7128d35ce95.svg#gh-dark-mode-only)

<div align="center">
   <p><strong>This is an unofficial SDK for the OpenAI API.</strong> The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or code. We offer a spectrum of models with different levels of power suitable for different tasks, as well as the ability to fine-tune your own custom models. These models can be used for everything from content generation to semantic search and classification.</p>
   <a href="https://github.com/speakeasy-sdks/openai-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/openai-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://platform.openai.com/docs/introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=2ca47c&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install openai-python
```
<!-- End SDK Installation [installation] -->

## Authentication

The OpenAI API uses API keys for authentication. Visit your API Keys page to retrieve the API key you'll use in your requests.

**Remember that your API key is a secret!** Do not share it with others or expose it in any client-side code (browsers, apps). Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an Authorization HTTP header as follows:

```bash
Authorization: Bearer YOUR_API_KEY
```

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [assistants](docs/sdks/assistants/README.md)

* [cancel_run](docs/sdks/assistants/README.md#cancel_run) - Cancels a run that is `in_progress`.
* [create_assistant](docs/sdks/assistants/README.md#create_assistant) - Create an assistant with a model and instructions.
* [create_assistant_file](docs/sdks/assistants/README.md#create_assistant_file) - Create an assistant file by attaching a [File](/docs/api-reference/files) to an [assistant](/docs/api-reference/assistants).
* [create_message](docs/sdks/assistants/README.md#create_message) - Create a message.
* [create_run](docs/sdks/assistants/README.md#create_run) - Create a run.
* [create_thread](docs/sdks/assistants/README.md#create_thread) - Create a thread.
* [create_thread_and_run](docs/sdks/assistants/README.md#create_thread_and_run) - Create a thread and run it in one request.
* [delete_assistant](docs/sdks/assistants/README.md#delete_assistant) - Delete an assistant.
* [delete_assistant_file](docs/sdks/assistants/README.md#delete_assistant_file) - Delete an assistant file.
* [delete_thread](docs/sdks/assistants/README.md#delete_thread) - Delete a thread.
* [get_assistant](docs/sdks/assistants/README.md#get_assistant) - Retrieves an assistant.
* [get_assistant_file](docs/sdks/assistants/README.md#get_assistant_file) - Retrieves an AssistantFile.
* [get_message](docs/sdks/assistants/README.md#get_message) - Retrieve a message.
* [get_message_file](docs/sdks/assistants/README.md#get_message_file) - Retrieves a message file.
* [get_run](docs/sdks/assistants/README.md#get_run) - Retrieves a run.
* [get_run_step](docs/sdks/assistants/README.md#get_run_step) - Retrieves a run step.
* [get_thread](docs/sdks/assistants/README.md#get_thread) - Retrieves a thread.
* [list_assistant_files](docs/sdks/assistants/README.md#list_assistant_files) - Returns a list of assistant files.
* [list_assistants](docs/sdks/assistants/README.md#list_assistants) - Returns a list of assistants.
* [list_message_files](docs/sdks/assistants/README.md#list_message_files) - Returns a list of message files.
* [list_messages](docs/sdks/assistants/README.md#list_messages) - Returns a list of messages for a given thread.
* [list_run_steps](docs/sdks/assistants/README.md#list_run_steps) - Returns a list of run steps belonging to a run.
* [list_runs](docs/sdks/assistants/README.md#list_runs) - Returns a list of runs belonging to a thread.
* [modify_assistant](docs/sdks/assistants/README.md#modify_assistant) - Modifies an assistant.
* [modify_message](docs/sdks/assistants/README.md#modify_message) - Modifies a message.
* [modify_run](docs/sdks/assistants/README.md#modify_run) - Modifies a run.
* [modify_thread](docs/sdks/assistants/README.md#modify_thread) - Modifies a thread.
* [submit_tool_ouputs_to_run](docs/sdks/assistants/README.md#submit_tool_ouputs_to_run) - When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.


### [audio](docs/sdks/audio/README.md)

* [create_speech](docs/sdks/audio/README.md#create_speech) - Generates audio from the input text.
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

* [create_file](docs/sdks/files/README.md#create_file) - Upload a file that can be used across various endpoints. The size of all the files uploaded by one organization can be up to 100 GB.

The size of individual files can be a maximum of 512 MB. See the [Assistants Tools guide](/docs/assistants/tools) to learn more about the types of files supported. The Fine-tuning API only supports `.jsonl` files.

Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

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
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = None
try:
    res = s.assistants.cancel_run(run_id='string', thread_id='string')
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.run_object is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.openai.com/v1` | None |

#### Example

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    server_idx=0,
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    server_url="https://api.openai.com/v1",
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import gpt
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = gpt.Gpt(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | http           | HTTP Bearer    |

To authenticate with the API the `api_key_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
