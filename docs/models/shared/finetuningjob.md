# FineTuningJob

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.



## Fields

| Field                                                                                                                                                    | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_at`                                                                                                                                             | *int*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The Unix timestamp (in seconds) for when the fine-tuning job was created.                                                                                |
| `error`                                                                                                                                                  | [FineTuningJobError](../../models/shared/finetuningjoberror.md)                                                                                          | :heavy_check_mark:                                                                                                                                       | For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.                                                 |
| `fine_tuned_model`                                                                                                                                       | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.                                  |
| `finished_at`                                                                                                                                            | *Optional[int]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                       | The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.               |
| `hyperparameters`                                                                                                                                        | [FineTuningJobHyperparameters](../../models/shared/finetuningjobhyperparameters.md)                                                                      | :heavy_check_mark:                                                                                                                                       | The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.                                |
| `id`                                                                                                                                                     | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The object identifier, which can be referenced in the API endpoints.                                                                                     |
| `model`                                                                                                                                                  | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The base model that is being fine-tuned.                                                                                                                 |
| `object`                                                                                                                                                 | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The object type, which is always "fine_tuning.job".                                                                                                      |
| `organization_id`                                                                                                                                        | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The organization that owns the fine-tuning job.                                                                                                          |
| `result_files`                                                                                                                                           | list[*str*]                                                                                                                                              | :heavy_check_mark:                                                                                                                                       | The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents). |
| `status`                                                                                                                                                 | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The current status of the fine-tuning job, which can be either `created`, `pending`, `running`, `succeeded`, `failed`, or `cancelled`.                   |
| `trained_tokens`                                                                                                                                         | *int*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.                   |
| `training_file`                                                                                                                                          | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).                     |
| `validation_file`                                                                                                                                        | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).              |