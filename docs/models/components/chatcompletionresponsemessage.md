# ChatCompletionResponseMessage

A chat completion message generated by the model.


## Fields

| Field                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content`                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                       | The contents of the message.                                                                                                                                                                                                                             |
| ~~`function_call`~~                                                                                                                                                                                                                                      | [Optional[components.ChatCompletionResponseMessageFunctionCall]](../../models/components/chatcompletionresponsemessagefunctioncall.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                       | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model. |
| `role`                                                                                                                                                                                                                                                   | [components.ChatCompletionResponseMessageRole](../../models/components/chatcompletionresponsemessagerole.md)                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                       | The role of the author of this message.                                                                                                                                                                                                                  |
| `tool_calls`                                                                                                                                                                                                                                             | List[[components.ChatCompletionMessageToolCall](../../models/components/chatcompletionmessagetoolcall.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                       | The tool calls generated by the model, such as function calls.                                                                                                                                                                                           |