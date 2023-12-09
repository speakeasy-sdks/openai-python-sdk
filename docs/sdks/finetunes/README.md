# FineTunes
(*fine_tunes*)

## Overview

Manage legacy fine-tuning jobs to tailor a model to your specific training data.

### Available Operations

* [~~cancel_fine_tune~~](#cancel_fine_tune) - Immediately cancel a fine-tune job.
 :warning: **Deprecated**
* [~~create_fine_tune~~](#create_fine_tune) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**
* [~~list_fine_tune_events~~](#list_fine_tune_events) - Get fine-grained status updates for a fine-tune job.
 :warning: **Deprecated**
* [~~list_fine_tunes~~](#list_fine_tunes) - List your organization's fine-tuning jobs
 :warning: **Deprecated**
* [~~retrieve_fine_tune~~](#retrieve_fine_tune) - Gets info about the fine-tune job.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)
 :warning: **Deprecated**

## ~~cancel_fine_tune~~

Immediately cancel a fine-tune job.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tunes.cancel_fine_tune(fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F')

if res.fine_tune is not None:
    # handle response
    pass
```

### Parameters

| Parameter                              | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `fine_tune_id`                         | *str*                                  | :heavy_check_mark:                     | The ID of the fine-tune job to cancel<br/> | ft-AF1WoRqd3aJAHsqc9NY7iL8F            |


### Response

**[operations.CancelFineTuneResponse](../../models/operations/cancelfinetuneresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## ~~create_fine_tune~~

Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateFineTuneRequest(
    classification_betas=[
        0.6,
        1,
        1.5,
        2,
    ],
    hyperparameters=components.Hyperparameters(
        n_epochs=399302,
    ),
    model=components.CreateFineTuneRequest2.CURIE,
    training_file='file-abc123',
    validation_file='file-abc123',
)

res = s.fine_tunes.create_fine_tune(req)

if res.fine_tune is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.CreateFineTuneRequest](../../models/components/createfinetunerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateFineTuneResponse](../../models/operations/createfinetuneresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## ~~list_fine_tune_events~~

Get fine-grained status updates for a fine-tune job.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tunes.list_fine_tune_events(fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F', stream=False)

if res.list_fine_tune_events_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fine_tune_id`                                                                                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                      | The ID of the fine-tune job to get events for.<br/>                                                                                                                                                                                                                                                                                                                                                                                                     | ft-AF1WoRqd3aJAHsqc9NY7iL8F                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stream`                                                                                                                                                                                                                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                      | Whether to stream events for the fine-tune job. If set to true,<br/>events will be sent as data-only<br/>[server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)<br/>as they become available. The stream will terminate with a<br/>`data: [DONE]` message when the job is finished (succeeded, cancelled,<br/>or failed).<br/><br/>If set to false, only events generated so far will be returned.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |


### Response

**[operations.ListFineTuneEventsResponse](../../models/operations/listfinetuneeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## ~~list_fine_tunes~~

List your organization's fine-tuning jobs


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tunes.list_fine_tunes()

if res.list_fine_tunes_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListFineTunesResponse](../../models/operations/listfinetunesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## ~~retrieve_fine_tune~~

Gets info about the fine-tune job.

[Learn more about fine-tuning](/docs/guides/legacy-fine-tuning)


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tunes.retrieve_fine_tune(fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F')

if res.fine_tune is not None:
    # handle response
    pass
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  | Example                      |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `fine_tune_id`               | *str*                        | :heavy_check_mark:           | The ID of the fine-tune job<br/> | ft-AF1WoRqd3aJAHsqc9NY7iL8F  |


### Response

**[operations.RetrieveFineTuneResponse](../../models/operations/retrievefinetuneresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
