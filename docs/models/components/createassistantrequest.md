# CreateAssistantRequest


## Fields

| Field                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                          | The description of the assistant. The maximum length is 512 characters.<br/>                                                                                                                                                                                |
| `file_ids`                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                          | A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.<br/>                                                 |
| `instructions`                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                          | The system instructions that the assistant uses. The maximum length is 32768 characters.<br/>                                                                                                                                                               |
| `metadata`                                                                                                                                                                                                                                                  | [Optional[components.CreateAssistantRequestMetadata]](../../models/components/createassistantrequestmetadata.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                          | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.<br/> |
| `model`                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                          | ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.<br/>                                           |
| `name`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                          | The name of the assistant. The maximum length is 256 characters.<br/>                                                                                                                                                                                       |
| `tools`                                                                                                                                                                                                                                                     | List[[Union[components.CodeInterpreterTool, components.RetrievalTool, components.FunctionTool]](../../models/components/createassistantrequesttools.md)]                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                          | A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.<br/>                                                                                      |