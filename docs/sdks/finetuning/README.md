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
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CancelFineTuningJobRequest(
    fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.fine_tuning.cancel_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CancelFineTuningJobRequest](../../models/operations/cancelfinetuningjobrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CancelFineTuningJobResponse](../../models/operations/cancelfinetuningjobresponse.md)**


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
    shared.CreateFineTuningJobRequestHyperparametersNEpochs1.AUTO,
    ),
shared.CreateFineTuningJobRequestModel2.GPT_3_5_TURBO,
    training_file='file-abc123',
    validation_file='file-abc123',
)

res = s.fine_tuning.create_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.CreateFineTuningJobRequest](../../models/shared/createfinetuningjobrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateFineTuningJobResponse](../../models/operations/createfinetuningjobresponse.md)**


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
    fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.fine_tuning.list_fine_tuning_events(req)

if res.list_fine_tuning_job_events_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListFineTuningEventsRequest](../../models/operations/listfinetuningeventsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ListFineTuningEventsResponse](../../models/operations/listfinetuningeventsresponse.md)**


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

req = operations.ListPaginatedFineTuningJobsRequest()

res = s.fine_tuning.list_paginated_fine_tuning_jobs(req)

if res.list_paginated_fine_tuning_jobs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListPaginatedFineTuningJobsRequest](../../models/operations/listpaginatedfinetuningjobsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ListPaginatedFineTuningJobsResponse](../../models/operations/listpaginatedfinetuningjobsresponse.md)**


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

res = s.fine_tuning.retrieve_fine_tuning_job(req)

if res.fine_tuning_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RetrieveFineTuningJobRequest](../../models/operations/retrievefinetuningjobrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RetrieveFineTuningJobResponse](../../models/operations/retrievefinetuningjobresponse.md)**

