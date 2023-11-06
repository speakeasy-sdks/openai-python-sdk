# Files
(*files*)

## Overview

Files are used to upload documents that can be used with features like fine-tuning.

### Available Operations

* [create_file](#create_file) - Upload a file that can be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please [contact us](https://help.openai.com/) if you need to increase the storage limit.

* [delete_file](#delete_file) - Delete a file.
* [download_file](#download_file) - Returns the contents of the specified file.
* [list_files](#list_files) - Returns a list of files that belong to the user's organization.
* [retrieve_file](#retrieve_file) - Returns information about a specific file.

## create_file

Upload a file that can be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please [contact us](https://help.openai.com/) if you need to increase the storage limit.


### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    api_key_auth="",
)

req = shared.CreateFileRequest(
    file=shared.CreateFileRequestFile(
        content='`\'$Z`(L/RH'.encode(),
        file='string',
    ),
    purpose='string',
)

res = s.files.create_file(req)

if res.open_ai_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateFileRequest](../../models/shared/createfilerequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateFileResponse](../../models/operations/createfileresponse.md)**


## delete_file

Delete a file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

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


## download_file

Returns the contents of the specified file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.download_file(file_id='string')

if res.download_file_200_application_json_string is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `file_id`                                   | *str*                                       | :heavy_check_mark:                          | The ID of the file to use for this request. |


### Response

**[operations.DownloadFileResponse](../../models/operations/downloadfileresponse.md)**


## list_files

Returns a list of files that belong to the user's organization.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    api_key_auth="",
)


res = s.files.list_files()

if res.list_files_response is not None:
    # handle response
    pass
```


### Response

**[operations.ListFilesResponse](../../models/operations/listfilesresponse.md)**


## retrieve_file

Returns information about a specific file.

### Example Usage

```python
import gpt
from gpt.models import operations, shared

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

