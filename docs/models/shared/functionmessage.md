# ~~FunctionMessage~~

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `content`                                                        | *Optional[str]*                                                  | :heavy_check_mark:                                               | The return value from the function call, to return to the model. |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | The name of the function to call.                                |
| `role`                                                           | [components.SchemasRole](../../models/shared/schemasrole.md)     | :heavy_check_mark:                                               | The role of the messages author, in this case `function`.        |