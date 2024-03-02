# Assistants
(*assistants*)

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
* [modify_assistant](#modify_assistant) - Modifies an assistant.
* [modify_message](#modify_message) - Modifies a message.
* [modify_run](#modify_run) - Modifies a run.
* [modify_thread](#modify_thread) - Modifies a thread.
* [submit_tool_ouputs_to_run](#submit_tool_ouputs_to_run) - When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.


## cancel_run

Cancels a run that is `in_progress`.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='<value>', thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_assistant

Create an assistant with a model and instructions.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateAssistantRequest(
    model='XTS',
)

res = s.assistants.create_assistant(req)

if res.assistant_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateAssistantRequest](../../models/components/createassistantrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateAssistantResponse](../../models/operations/createassistantresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_assistant_file

Create an assistant file by attaching a [File](/docs/api-reference/files) to an [assistant](/docs/api-reference/assistants).

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.create_assistant_file(create_assistant_file_request=components.CreateAssistantFileRequest(
    file_id='<value>',
), assistant_id='file-abc123')

if res.assistant_file_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `create_assistant_file_request`                                                                | [components.CreateAssistantFileRequest](../../models/components/createassistantfilerequest.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `assistant_id`                                                                                 | *str*                                                                                          | :heavy_check_mark:                                                                             | The ID of the assistant for which to create a File.<br/>                                       | file-abc123                                                                                    |


### Response

**[operations.CreateAssistantFileResponse](../../models/operations/createassistantfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_message

Create a message.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.create_message(create_message_request=components.CreateMessageRequest(
    content='<value>',
    role=components.CreateMessageRequestRole.USER,
), thread_id='<value>')

if res.message_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `create_message_request`                                                           | [components.CreateMessageRequest](../../models/components/createmessagerequest.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `thread_id`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | The ID of the [thread](/docs/api-reference/threads) to create a message for.       |


### Response

**[operations.CreateMessageResponse](../../models/operations/createmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_run

Create a run.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.create_run(create_run_request=components.CreateRunRequest(
    assistant_id='<value>',
), thread_id='<value>')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `create_run_request`                                                       | [components.CreateRunRequest](../../models/components/createrunrequest.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `thread_id`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the thread to run.                                               |


### Response

**[operations.CreateRunResponse](../../models/operations/createrunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_thread

Create a thread.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateThreadRequest()

res = s.assistants.create_thread(req)

if res.thread_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.CreateThreadRequest](../../models/components/createthreadrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateThreadResponse](../../models/operations/createthreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_thread_and_run

Create a thread and run it in one request.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateThreadAndRunRequest(
    assistant_id='<value>',
)

res = s.assistants.create_thread_and_run(req)

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.CreateThreadAndRunRequest](../../models/components/createthreadandrunrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateThreadAndRunResponse](../../models/operations/createthreadandrunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_assistant

Delete an assistant.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.delete_assistant(assistant_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_assistant_file

Delete an assistant file.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.delete_assistant_file(assistant_id='<value>', file_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_thread

Delete a thread.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.delete_thread(thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_assistant

Retrieves an assistant.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_assistant(assistant_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_assistant_file

Retrieves an AssistantFile.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_assistant_file(assistant_id='<value>', file_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_message

Retrieve a message.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_message(message_id='<value>', thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_message_file

Retrieves a message file.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_message_file(file_id='file-abc123', message_id='msg_abc123', thread_id='thread_abc123')

if res.message_file_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `file_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | The ID of the file being retrieved.                        | file-abc123                                                |
| `message_id`                                               | *str*                                                      | :heavy_check_mark:                                         | The ID of the message the file belongs to.                 | msg_abc123                                                 |
| `thread_id`                                                | *str*                                                      | :heavy_check_mark:                                         | The ID of the thread to which the message and File belong. | thread_abc123                                              |


### Response

**[operations.GetMessageFileResponse](../../models/operations/getmessagefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_run

Retrieves a run.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_run(run_id='<value>', thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_run_step

Retrieves a run step.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_run_step(run_id='<value>', step_id='<value>', thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_thread

Retrieves a thread.

### Example Usage

```python
import gpt

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.get_thread(thread_id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_assistant_files

Returns a list of assistant files.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListAssistantFilesRequest(
    assistant_id='<value>',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_assistants

Returns a list of assistants.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.list_assistants(after='<value>', before='<value>', limit=20, order=operations.QueryParamOrder.DESC)

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_message_files

Returns a list of message files.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListMessageFilesRequest(
    message_id='<value>',
    thread_id='<value>',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_messages

Returns a list of messages for a given thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListMessagesRequest(
    thread_id='<value>',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_run_steps

Returns a list of run steps belonging to a run.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListRunStepsRequest(
    run_id='<value>',
    thread_id='<value>',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_runs

Returns a list of runs belonging to a thread.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListRunsRequest(
    thread_id='<value>',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## modify_assistant

Modifies an assistant.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.modify_assistant(modify_assistant_request=components.ModifyAssistantRequest(), assistant_id='<value>')

if res.assistant_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `modify_assistant_request`                                                             | [components.ModifyAssistantRequest](../../models/components/modifyassistantrequest.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `assistant_id`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | The ID of the assistant to modify.                                                     |


### Response

**[operations.ModifyAssistantResponse](../../models/operations/modifyassistantresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## modify_message

Modifies a message.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.modify_message(modify_message_request=components.ModifyMessageRequest(), message_id='<value>', thread_id='<value>')

if res.message_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `modify_message_request`                                                           | [components.ModifyMessageRequest](../../models/components/modifymessagerequest.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `message_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | The ID of the message to modify.                                                   |
| `thread_id`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | The ID of the thread to which this message belongs.                                |


### Response

**[operations.ModifyMessageResponse](../../models/operations/modifymessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## modify_run

Modifies a run.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.modify_run(modify_run_request=components.ModifyRunRequest(), run_id='<value>', thread_id='<value>')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `modify_run_request`                                                       | [components.ModifyRunRequest](../../models/components/modifyrunrequest.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `run_id`                                                                   | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the run to modify.                                               |
| `thread_id`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the [thread](/docs/api-reference/threads) that was run.          |


### Response

**[operations.ModifyRunResponse](../../models/operations/modifyrunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## modify_thread

Modifies a thread.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.modify_thread(modify_thread_request=components.ModifyThreadRequest(), thread_id='<value>')

if res.thread_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `modify_thread_request`                                                          | [components.ModifyThreadRequest](../../models/components/modifythreadrequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `thread_id`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the thread to modify. Only the `metadata` can be modified.             |


### Response

**[operations.ModifyThreadResponse](../../models/operations/modifythreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## submit_tool_ouputs_to_run

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.


### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.submit_tool_ouputs_to_run(submit_tool_outputs_run_request=components.SubmitToolOutputsRunRequest(
    tool_outputs=[
        components.ToolOutputs(),
    ],
), run_id='<value>', thread_id='<value>')

if res.run_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `submit_tool_outputs_run_request`                                                                | [components.SubmitToolOutputsRunRequest](../../models/components/submittooloutputsrunrequest.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `run_id`                                                                                         | *str*                                                                                            | :heavy_check_mark:                                                                               | The ID of the run that requires the tool output submission.                                      |
| `thread_id`                                                                                      | *str*                                                                                            | :heavy_check_mark:                                                                               | The ID of the [thread](/docs/api-reference/threads) to which this run belongs.                   |


### Response

**[operations.SubmitToolOuputsToRunResponse](../../models/operations/submittoolouputstorunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
