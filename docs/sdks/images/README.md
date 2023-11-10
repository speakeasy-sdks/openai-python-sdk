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
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateImageRequest(
components.CreateImageRequest2.DALL_E_3,
    n=1,
    prompt='A cute baby sea otter',
    quality=components.Quality.STANDARD,
    response_format=components.CreateImageRequestResponseFormat.URL,
    size=components.CreateImageRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    style=components.Style.VIVID,
    user='user-1234',
)

res = s.images.create_image(req)

if res.images_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.CreateImageRequest](../../models/components/createimagerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateImageResponse](../../models/operations/createimageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_image_edit

Creates an edited or extended image given an original image and a prompt.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateImageEditRequest(
    image=components.CreateImageEditRequestImage(
        content='0x3e31F4cec5'.encode(),
        file_name='facilitator_gosh_hatchback.mpe',
    ),
    mask=components.Mask(
        content='0xFC5456e4eC'.encode(),
        file_name='electric_cambridgeshire.jpeg',
    ),
components.CreateImageEditRequest2.DALL_E_2,
    n=1,
    prompt='A cute baby sea otter wearing a beret',
    response_format=components.CreateImageEditRequestResponseFormat.URL,
    size=components.Size.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.images.create_image_edit(req)

if res.images_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateImageEditRequest](../../models/components/createimageeditrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateImageEditResponse](../../models/operations/createimageeditresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_image_variation

Creates a variation of a given image.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateImageVariationRequest(
    image=components.CreateImageVariationRequestImage(
        content='0xfdd5b8DcDa'.encode(),
        file_name='fantastic.gif',
    ),
components.CreateImageVariationRequest2.DALL_E_2,
    n=1,
    response_format=components.CreateImageVariationRequestResponseFormat.URL,
    size=components.CreateImageVariationRequestSize.ONE_THOUSAND_AND_TWENTY_FOURX1024,
    user='user-1234',
)

res = s.images.create_image_variation(req)

if res.images_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.CreateImageVariationRequest](../../models/components/createimagevariationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateImageVariationResponse](../../models/operations/createimagevariationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
