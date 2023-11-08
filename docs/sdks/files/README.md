# Files
(*.files*)

## Overview

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

### Available Operations

* [create_file](#create_file) - Upload a file that can be used across various endpoints/features. The size of all the files uploaded by one organization can be up to 100 GB.

The size of individual files for can be a maximum of 512MB. See the [Assistants Tools guide](/docs/assistants/tools) to learn more about the types of files supported. The Fine-tuning API only supports `.jsonl` files.

Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

* [delete_file](#delete_file) - Delete a file.
* [download_file](#download_file) - Returns the contents of the specified file.
* [list_files](#list_files) - Returns a list of files that belong to the user's organization.
* [retrieve_file](#retrieve_file) - Returns information about a specific file.

## create_file

Upload a file that can be used across various endpoints/features. The size of all the files uploaded by one organization can be up to 100 GB.

The size of individual files for can be a maximum of 512MB. See the [Assistants Tools guide](/docs/assistants/tools) to learn more about the types of files supported. The Fine-tuning API only supports `.jsonl` files.

Please [contact us](https://help.openai.com/) if you need to increase these storage limits.


### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateFileRequest(
    file=components.File(
        content='0xf10df1a3b9'.encode(),
        file_name='rap_national.mp4v',
    ),
    purpose=components.Purpose.FINE_TUNE,
)

res = s.files.create_file(req)

if res.open_ai_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.CreateFileRequest](../../models/shared/createfilerequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateFileResponse](../../models/operations/createfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_file

Delete a file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.delete_file(file_id='string')

if res.delete_file_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `file_id`                                   | *str*                                       | :heavy_check_mark:                          | The ID of the file to use for this request. |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## download_file

Returns the contents of the specified file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.download_file(file_id='string')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `file_id`                                   | *str*                                       | :heavy_check_mark:                          | The ID of the file to use for this request. |


### Response

**[operations.DownloadFileResponse](../../models/operations/downloadfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_files

Returns a list of files that belong to the user's organization.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.list_files(purpose='string')

if res.list_files_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `purpose`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | Only return files with the given purpose. |


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.retrieve_file(file_id='string')

if res.open_ai_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `file_id`                                   | *str*                                       | :heavy_check_mark:                          | The ID of the file to use for this request. |


### Response

**[operations.RetrieveFileResponse](../../models/operations/retrievefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
