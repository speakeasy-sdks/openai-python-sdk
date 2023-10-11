# Images
(*images*)

## Overview

Given a prompt and/or an input image, the model will generate a new image.

### Available Operations

* [create_image](#create_image) - Creates an image given a prompt.
* [create_image_edit](#create_image_edit) - Creates an edited or extended image given an original image and a prompt.
* [create_image_variation](#create_image_variation) - Creates a variation of a given image.

## create_image

Creates an image given a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageRequest(
    n=1,
    prompt='A cute baby sea otter',
    response_format=shared.CreateImageRequestResponseFormat.URL,
    size=shared.CreateImageRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.images.create_image(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CreateImageRequest](../../models/shared/createimagerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateImageResponse](../../models/operations/createimageresponse.md)**


## create_image_edit

Creates an edited or extended image given an original image and a prompt.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageEditRequest(
    image=shared.CreateImageEditRequestImage(
        content='0]/(|3W_T9'.encode(),
        image='https://loremflickr.com/640/480',
    ),
    mask=shared.CreateImageEditRequestMask(
        content='`^YjrpxopK'.encode(),
        mask='Rap Dodge Incredible',
    ),
    n=1,
    prompt='A cute baby sea otter wearing a beret',
    response_format=shared.CreateImageEditRequestResponseFormat.URL,
    size=shared.CreateImageEditRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.images.create_image_edit(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateImageEditRequest](../../models/shared/createimageeditrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateImageEditResponse](../../models/operations/createimageeditresponse.md)**


## create_image_variation

Creates a variation of a given image.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateImageVariationRequest(
    image=shared.CreateImageVariationRequestImage(
        content='`YY7PCrWuK'.encode(),
        image='https://loremflickr.com/640/480',
    ),
    n=1,
    response_format=shared.CreateImageVariationRequestResponseFormat.URL,
    size=shared.CreateImageVariationRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.images.create_image_variation(req)

if res.images_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateImageVariationRequest](../../models/shared/createimagevariationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateImageVariationResponse](../../models/operations/createimagevariationresponse.md)**

