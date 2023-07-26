# FineTune

OK


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `created_at`                                                      | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `events`                                                          | list[[FineTuneEvent](../../models/shared/finetuneevent.md)]       | :heavy_minus_sign:                                                | N/A                                                               |
| `fine_tuned_model`                                                | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `hyperparams`                                                     | [FineTuneHyperparams](../../models/shared/finetunehyperparams.md) | :heavy_check_mark:                                                | N/A                                                               |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `model`                                                           | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `object`                                                          | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `organization_id`                                                 | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `result_files`                                                    | list[[OpenAIFile](../../models/shared/openaifile.md)]             | :heavy_check_mark:                                                | N/A                                                               |
| `status`                                                          | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `training_files`                                                  | list[[OpenAIFile](../../models/shared/openaifile.md)]             | :heavy_check_mark:                                                | N/A                                                               |
| `updated_at`                                                      | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `validation_files`                                                | list[[OpenAIFile](../../models/shared/openaifile.md)]             | :heavy_check_mark:                                                | N/A                                                               |