# FineTuning
(*fine_tuning*)

## Overview

Manage fine-tuning jobs to tailor a model to your specific training data.

### Available Operations

* [cancel_fine_tuning_job](#cancel_fine_tuning_job) - Immediately cancel a fine-tune job.

* [create_fine_tuning_job](#create_fine_tuning_job) - Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)

* [list_fine_tuning_events](#list_fine_tuning_events) - Get status updates for a fine-tuning job.

* [list_paginated_fine_tuning_jobs](#list_paginated_fine_tuning_jobs) - List your organization's fine-tuning jobs

* [retrieve_fine_tuning_job](#retrieve_fine_tuning_job) - Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


## cancel_fine_tuning_job

Immediately cancel a fine-tune job.


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tuning.cancel_fine_tuning_job(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F')

if res.fine_tuning_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `fine_tuning_job_id`                      | *str*                                     | :heavy_check_mark:                        | The ID of the fine-tuning job to cancel.<br/> | ft-AF1WoRqd3aJAHsqc9NY7iL8F               |


### Response

**[operations.CancelFineTuningJobResponse](../../models/operations/cancelfinetuningjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_fine_tuning_job

Creates a job that fine-tunes a specified model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateFineTuningJobRequest(
    hyperparameters=components.CreateFineTuningJobRequestHyperparameters(
        batch_size=components.CreateFineTuningJobRequest1.AUTO,
        learning_rate_multiplier=components.CreateFineTuningJobRequestSchemas1.AUTO,
        n_epochs=components.CreateFineTuningJobRequestSchemasHyperparameters1.AUTO,
    ),
    model=components.CreateFineTuningJobRequest2.GPT_3_5_TURBO,
    training_file='file-abc123',
    validation_file='file-abc123',
)

res = s.fine_tuning.create_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.CreateFineTuningJobRequest](../../models/components/createfinetuningjobrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreateFineTuningJobResponse](../../models/operations/createfinetuningjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_fine_tuning_events

Get status updates for a fine-tuning job.


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tuning.list_fine_tuning_events(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F', after='string', limit=896841)

if res.list_fine_tuning_job_events_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `fine_tuning_job_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the fine-tuning job to get events for.<br/>               | ft-AF1WoRqd3aJAHsqc9NY7iL8F                                         |
| `after`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Identifier for the last event from the previous pagination request. |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of events to retrieve.                                       |                                                                     |


### Response

**[operations.ListFineTuningEventsResponse](../../models/operations/listfinetuningeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_paginated_fine_tuning_jobs

List your organization's fine-tuning jobs


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tuning.list_paginated_fine_tuning_jobs(after='string', limit=385496)

if res.list_paginated_fine_tuning_jobs_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `after`                                                           | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Identifier for the last job from the previous pagination request. |
| `limit`                                                           | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Number of fine-tuning jobs to retrieve.                           |


### Response

**[operations.ListPaginatedFineTuningJobsResponse](../../models/operations/listpaginatedfinetuningjobsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## retrieve_fine_tuning_job

Get info about a fine-tuning job.

[Learn more about fine-tuning](/docs/guides/fine-tuning)


### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.fine_tuning.retrieve_fine_tuning_job(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F')

if res.fine_tuning_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     | Example                         |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `fine_tuning_job_id`            | *str*                           | :heavy_check_mark:              | The ID of the fine-tuning job.<br/> | ft-AF1WoRqd3aJAHsqc9NY7iL8F     |


### Response

**[operations.RetrieveFineTuningJobResponse](../../models/operations/retrievefinetuningjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
