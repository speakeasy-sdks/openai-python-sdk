# AssistantFileObject

A list of [Files](/docs/api-reference/files) attached to an `assistant`.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `assistant_id`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | The assistant ID that the file is attached to.                           |
| `created_at`                                                             | *int*                                                                    | :heavy_check_mark:                                                       | The Unix timestamp (in seconds) for when the assistant file was created. |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | The identifier, which can be referenced in API endpoints.                |
| `object`                                                                 | [components.Object](../../models/shared/object.md)                       | :heavy_check_mark:                                                       | The object type, which is always `assistant.file`.                       |