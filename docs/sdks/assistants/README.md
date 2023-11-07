# Assistants
(*.assistants*)

## Overview

Build Assistants that can call models and use tools.

### Available Operations

* [cancel_run](#cancel_run) - Cancels a run that is `in_progress`.
* [create_assistant](#create_assistant) - Create an assistant with a model and instructions.
* [create_assistant_file](#create_assistant_file) - Create an assistant file by attaching a [File](/docs/api-reference/files) to an [assistant](/docs/api-reference/assistants).
* [create_message](#create_message) - Create a message.
* [create_run](#create_run) - Create a run.
* [create_thread](#create_thread) - Create a thread.
* [create_thread_and_run](#create_thread_and_run) - Create a thread and run it in one request.
* [delete_assistant](#delete_assistant) - Delete an assistant.
* [delete_assistant_file](#delete_assistant_file) - Delete an assistant file.
* [delete_thread](#delete_thread) - Delete a thread.
* [get_assistant](#get_assistant) - Retrieves an assistant.
* [get_assistant_file](#get_assistant_file) - Retrieves an AssistantFile.
* [get_message](#get_message) - Retrieve a message.
* [get_message_file](#get_message_file) - Retrieves a message file.
* [get_run](#get_run) - Retrieves a run.
* [get_run_step](#get_run_step) - Retrieves a run step.
* [get_thread](#get_thread) - Retrieves a thread.
* [list_assistant_files](#list_assistant_files) - Returns a list of assistant files.
* [list_assistants](#list_assistants) - Returns a list of assistants.
* [list_message_files](#list_message_files) - Returns a list of message files.
* [list_messages](#list_messages) - Returns a list of messages for a given thread.
* [list_run_steps](#list_run_steps) - Returns a list of run steps belonging to a run.
* [list_runs](#list_runs) - Returns a list of runs belonging to a thread.
* [modify_message](#modify_message) - Modifies a message.
* [modify_run](#modify_run) - Modifies a run.
* [modify_thread](#modify_thread) - Modifies a thread.
* [submit_tool_ouputs_to_run](#submit_tool_ouputs_to_run) - When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.


## cancel_run

Cancels a run that is `in_progress`.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `run_id`                                        | *str*                                           | :heavy_check_mark:                              | The ID of the run to cancel.                    |
| `thread_id`                                     | *str*                                           | :heavy_check_mark:                              | The ID of the thread to which this run belongs. |


### Response

**[operations.CancelRunResponse](../../models/operations/cancelrunresponse.md)**


## create_assistant

Create an assistant with a model and instructions.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateAssistantRequest(
    file_ids=[
        'string',
    ],
    metadata=components.CreateAssistantRequestMetadata(),
    model='XTS',
    tools=[
        components.RetrievalTool(
            type=components.SchemasAssistantToolsRetrievalType.RETRIEVAL,
        ),
    ],
)

res = s.assistants.create_assistant(req)

if res.assistant_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.CreateAssistantRequest](../../models/shared/createassistantrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateAssistantResponse](../../models/operations/createassistantresponse.md)**


## create_assistant_file

Create an assistant file by attaching a [File](/docs/api-reference/files) to an [assistant](/docs/api-reference/assistants).

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.create_assistant_file(create_assistant_file_request=components.CreateAssistantFileRequest(
    file_id='string',
), assistant_id='file-AF1WoRqd3aJAHsqc9NY7iL8F')

if res.assistant_file_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `create_assistant_file_request`                                                            | [components.CreateAssistantFileRequest](../../models/shared/createassistantfilerequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `assistant_id`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | The ID of the assistant for which to create a File.<br/>                                   | file-AF1WoRqd3aJAHsqc9NY7iL8F                                                              |


### Response

**[operations.CreateAssistantFileResponse](../../models/operations/createassistantfileresponse.md)**


## create_message

Create a message.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.create_message(create_message_request=components.CreateMessageRequest(
    content='string',
    file_ids=[
        'string',
    ],
    metadata=components.CreateMessageRequestMetadata(),
    role=components.CreateMessageRequestRole.USER,
), thread_id='string')

if res.message_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `create_message_request`                                                       | [components.CreateMessageRequest](../../models/shared/createmessagerequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `thread_id`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | The ID of the [thread](/docs/api-reference/threads) to create a message for.   |


### Response

**[operations.CreateMessageResponse](../../models/operations/createmessageresponse.md)**


## create_run

Create a run.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.create_run(create_run_request=components.CreateRunRequest(
    assistant_id='string',
    metadata=components.CreateRunRequestMetadata(),
    tools=[
        components.CodeInterpreterTool(
            type=components.Type.CODE_INTERPRETER,
        ),
    ],
), thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `create_run_request`                                                   | [components.CreateRunRequest](../../models/shared/createrunrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `thread_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the thread to run.                                           |


### Response

**[operations.CreateRunResponse](../../models/operations/createrunresponse.md)**


## create_thread

Create a thread.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateThreadRequest(
    messages=[
        components.CreateMessageRequest(
            content='string',
            file_ids=[
                'string',
            ],
            metadata=components.CreateMessageRequestMetadata(),
            role=components.CreateMessageRequestRole.USER,
        ),
    ],
    metadata=components.CreateThreadRequestMetadata(),
)

res = s.assistants.create_thread(req)

if res.thread_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.CreateThreadRequest](../../models/shared/createthreadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateThreadResponse](../../models/operations/createthreadresponse.md)**


## create_thread_and_run

Create a thread and run it in one request.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateThreadAndRunRequest(
    assistant_id='string',
    metadata=components.CreateThreadAndRunRequestMetadata(),
    thread=components.CreateThreadRequest(
        messages=[
            components.CreateMessageRequest(
                content='string',
                file_ids=[
                    'string',
                ],
                metadata=components.CreateMessageRequestMetadata(),
                role=components.CreateMessageRequestRole.USER,
            ),
        ],
        metadata=components.CreateThreadRequestMetadata(),
    ),
    tools=[
        components.AssistantToolsFunction(
            function=components.AssistantToolsFunctionFunction(
                description='Exclusive holistic moratorium',
                name='string',
                parameters={
                    "key": 'string',
                },
            ),
            type=components.AssistantToolsFunctionType.FUNCTION,
        ),
    ],
)

res = s.assistants.create_thread_and_run(req)

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.CreateThreadAndRunRequest](../../models/shared/createthreadandrunrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateThreadAndRunResponse](../../models/operations/createthreadandrunresponse.md)**


## delete_assistant

Delete an assistant.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.delete_assistant(assistant_id='string')

if res.delete_assistant_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                          | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `assistant_id`                     | *str*                              | :heavy_check_mark:                 | The ID of the assistant to delete. |


### Response

**[operations.DeleteAssistantResponse](../../models/operations/deleteassistantresponse.md)**


## delete_assistant_file

Delete an assistant file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.delete_assistant_file(assistant_id='string', file_id='string')

if res.delete_assistant_file_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                         | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `assistant_id`                                    | *str*                                             | :heavy_check_mark:                                | The ID of the assistant that the file belongs to. |
| `file_id`                                         | *str*                                             | :heavy_check_mark:                                | The ID of the file to delete.                     |


### Response

**[operations.DeleteAssistantFileResponse](../../models/operations/deleteassistantfileresponse.md)**


## delete_thread

Delete a thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.delete_thread(thread_id='string')

if res.delete_thread_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `thread_id`                     | *str*                           | :heavy_check_mark:              | The ID of the thread to delete. |


### Response

**[operations.DeleteThreadResponse](../../models/operations/deletethreadresponse.md)**


## get_assistant

Retrieves an assistant.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_assistant(assistant_id='string')

if res.assistant_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `assistant_id`                       | *str*                                | :heavy_check_mark:                   | The ID of the assistant to retrieve. |


### Response

**[operations.GetAssistantResponse](../../models/operations/getassistantresponse.md)**


## get_assistant_file

Retrieves an AssistantFile.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_assistant_file(assistant_id='string', file_id='string')

if res.assistant_file_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `assistant_id`                                   | *str*                                            | :heavy_check_mark:                               | The ID of the assistant who the file belongs to. |
| `file_id`                                        | *str*                                            | :heavy_check_mark:                               | The ID of the file we're getting.                |


### Response

**[operations.GetAssistantFileResponse](../../models/operations/getassistantfileresponse.md)**


## get_message

Retrieve a message.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_message(message_id='string', thread_id='string')

if res.message_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `message_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | The ID of the message to retrieve.                                                 |
| `thread_id`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | The ID of the [thread](/docs/api-reference/threads) to which this message belongs. |


### Response

**[operations.GetMessageResponse](../../models/operations/getmessageresponse.md)**


## get_message_file

Retrieves a message file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_message_file(file_id='file-AF1WoRqd3aJAHsqc9NY7iL8F', message_id='msg_AF1WoRqd3aJAHsqc9NY7iL8F', thread_id='thread_AF1WoRqd3aJAHsqc9NY7iL8F')

if res.message_file_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `file_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | The ID of the file being retrieved.                        | file-AF1WoRqd3aJAHsqc9NY7iL8F                              |
| `message_id`                                               | *str*                                                      | :heavy_check_mark:                                         | The ID of the message the file belongs to.                 | msg_AF1WoRqd3aJAHsqc9NY7iL8F                               |
| `thread_id`                                                | *str*                                                      | :heavy_check_mark:                                         | The ID of the thread to which the message and File belong. | thread_AF1WoRqd3aJAHsqc9NY7iL8F                            |


### Response

**[operations.GetMessageFileResponse](../../models/operations/getmessagefileresponse.md)**


## get_run

Retrieves a run.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `run_id`                                                          | *str*                                                             | :heavy_check_mark:                                                | The ID of the run to retrieve.                                    |
| `thread_id`                                                       | *str*                                                             | :heavy_check_mark:                                                | The ID of the [thread](/docs/api-reference/threads) that was run. |


### Response

**[operations.GetRunResponse](../../models/operations/getrunresponse.md)**


## get_run_step

Retrieves a run step.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_run_step(run_id='string', step_id='string', thread_id='string')

if res.run_step_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `run_id`                                                    | *str*                                                       | :heavy_check_mark:                                          | The ID of the run to which the run step belongs.            |
| `step_id`                                                   | *str*                                                       | :heavy_check_mark:                                          | The ID of the run step to retrieve.                         |
| `thread_id`                                                 | *str*                                                       | :heavy_check_mark:                                          | The ID of the thread to which the run and run step belongs. |


### Response

**[operations.GetRunStepResponse](../../models/operations/getrunstepresponse.md)**


## get_thread

Retrieves a thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.get_thread(thread_id='string')

if res.thread_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `thread_id`                       | *str*                             | :heavy_check_mark:                | The ID of the thread to retrieve. |


### Response

**[operations.GetThreadResponse](../../models/operations/getthreadresponse.md)**


## list_assistant_files

Returns a list of assistant files.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)

req = operations.ListAssistantFilesRequest(
    assistant_id='string',
)

res = s.assistants.list_assistant_files(req)

if res.list_assistant_files_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListAssistantFilesRequest](../../models/operations/listassistantfilesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListAssistantFilesResponse](../../models/operations/listassistantfilesresponse.md)**


## list_assistants

Returns a list of assistants.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.list_assistants(after='string', before='string', limit=948776, order=operations.QueryParamOrder.ASC)

if res.list_assistants_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.<br/>   |
| `before`                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.<br/> |
| `limit`                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.<br/>                                                                                                                                                                        |
| `order`                                                                                                                                                                                                                                                                                | [Optional[operations.QueryParamOrder]](../../models/operations/queryparamorder.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.<br/>                                                                                                                                                               |


### Response

**[operations.ListAssistantsResponse](../../models/operations/listassistantsresponse.md)**


## list_message_files

Returns a list of message files.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)

req = operations.ListMessageFilesRequest(
    message_id='string',
    thread_id='string',
)

res = s.assistants.list_message_files(req)

if res.list_message_files_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListMessageFilesRequest](../../models/operations/listmessagefilesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListMessageFilesResponse](../../models/operations/listmessagefilesresponse.md)**


## list_messages

Returns a list of messages for a given thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)

req = operations.ListMessagesRequest(
    thread_id='string',
)

res = s.assistants.list_messages(req)

if res.list_messages_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListMessagesRequest](../../models/operations/listmessagesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListMessagesResponse](../../models/operations/listmessagesresponse.md)**


## list_run_steps

Returns a list of run steps belonging to a run.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)

req = operations.ListRunStepsRequest(
    run_id='string',
    thread_id='string',
)

res = s.assistants.list_run_steps(req)

if res.list_run_steps_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListRunStepsRequest](../../models/operations/listrunstepsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListRunStepsResponse](../../models/operations/listrunstepsresponse.md)**


## list_runs

Returns a list of runs belonging to a thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)

req = operations.ListRunsRequest(
    thread_id='string',
)

res = s.assistants.list_runs(req)

if res.list_runs_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListRunsRequest](../../models/operations/listrunsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListRunsResponse](../../models/operations/listrunsresponse.md)**


## modify_message

Modifies a message.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.modify_message(modify_message_request=components.ModifyMessageRequest(
    metadata=components.ModifyMessageRequestMetadata(),
), message_id='string', thread_id='string')

if res.message_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `modify_message_request`                                                       | [components.ModifyMessageRequest](../../models/shared/modifymessagerequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `message_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | The ID of the message to modify.                                               |
| `thread_id`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | The ID of the thread to which this message belongs.                            |


### Response

**[operations.ModifyMessageResponse](../../models/operations/modifymessageresponse.md)**


## modify_run

Modifies a run.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.modify_run(modify_run_request=components.ModifyRunRequest(
    metadata=components.ModifyRunRequestMetadata(),
), run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `modify_run_request`                                                   | [components.ModifyRunRequest](../../models/shared/modifyrunrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `run_id`                                                               | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the run to modify.                                           |
| `thread_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the [thread](/docs/api-reference/threads) that was run.      |


### Response

**[operations.ModifyRunResponse](../../models/operations/modifyrunresponse.md)**


## modify_thread

Modifies a thread.

### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.modify_thread(modify_thread_request=components.ModifyThreadRequest(
    metadata=components.ModifyThreadRequestMetadata(),
), thread_id='string')

if res.thread_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `modify_thread_request`                                                      | [components.ModifyThreadRequest](../../models/shared/modifythreadrequest.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `thread_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | The ID of the thread to modify. Only the `metadata` can be modified.         |


### Response

**[operations.ModifyThreadResponse](../../models/operations/modifythreadresponse.md)**


## submit_tool_ouputs_to_run

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.


### Example Usage

```python
import gpt
from gpt.models import components, operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.submit_tool_ouputs_to_run(submit_tool_outputs_run_request=components.SubmitToolOutputsRunRequest(
    tool_outputs=[
        components.ToolOutputs(),
    ],
), run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `submit_tool_outputs_run_request`                                                            | [components.SubmitToolOutputsRunRequest](../../models/shared/submittooloutputsrunrequest.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `run_id`                                                                                     | *str*                                                                                        | :heavy_check_mark:                                                                           | The ID of the run that requires the tool output submission.                                  |
| `thread_id`                                                                                  | *str*                                                                                        | :heavy_check_mark:                                                                           | The ID of the [thread](/docs/api-reference/threads) to which this run belongs.               |


### Response

**[operations.SubmitToolOuputsToRunResponse](../../models/operations/submittoolouputstorunresponse.md)**

