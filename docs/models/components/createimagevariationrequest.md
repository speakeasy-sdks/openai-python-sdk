# CreateImageVariationRequest


## Fields

| Field                                                                                                                                                              | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `image`                                                                                                                                                            | [components.CreateImageVariationRequestImage](../../models/components/createimagevariationrequestimage.md)                                                         | :heavy_check_mark:                                                                                                                                                 | The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.                                                           |                                                                                                                                                                    |
| `model`                                                                                                                                                            | [Optional[Union[str, components.CreateImageVariationRequest2]]](../../models/components/createimagevariationrequestmodel.md)                                       | :heavy_minus_sign:                                                                                                                                                 | The model to use for image generation. Only `dall-e-2` is supported at this time.                                                                                  | dall-e-2                                                                                                                                                           |
| `n`                                                                                                                                                                | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.                                                               | 1                                                                                                                                                                  |
| `response_format`                                                                                                                                                  | [Optional[components.CreateImageVariationRequestResponseFormat]](../../models/components/createimagevariationrequestresponseformat.md)                             | :heavy_minus_sign:                                                                                                                                                 | The format in which the generated images are returned. Must be one of `url` or `b64_json`.                                                                         | url                                                                                                                                                                |
| `size`                                                                                                                                                             | [Optional[components.CreateImageVariationRequestSize]](../../models/components/createimagevariationrequestsize.md)                                                 | :heavy_minus_sign:                                                                                                                                                 | The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.                                                                             | 1024x1024                                                                                                                                                          |
| `user`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).<br/> | user-1234                                                                                                                                                          |