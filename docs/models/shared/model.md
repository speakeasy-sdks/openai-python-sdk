# Model

Describes an OpenAI model offering that can be used with the API.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `created`                                                           | *Optional[int]*                                                     | :heavy_check_mark:                                                  | The Unix timestamp (in seconds) when the model was created.         |
| `id`                                                                | *Optional[str]*                                                     | :heavy_check_mark:                                                  | The model identifier, which can be referenced in the API endpoints. |
| `object`                                                            | *Optional[str]*                                                     | :heavy_check_mark:                                                  | The object type, which is always "model".                           |
| `owned_by`                                                          | *Optional[str]*                                                     | :heavy_check_mark:                                                  | The organization that owns the model.                               |