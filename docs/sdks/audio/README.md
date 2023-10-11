# Audio
(*audio*)

## Overview

Learn how to turn audio into text.

### Available Operations

* [create_transcription](#create_transcription) - Transcribes audio into the input language.
* [create_translation](#create_translation) - Translates audio into English.

## create_transcription

Transcribes audio into the input language.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateTranscriptionRequest(
    file=shared.CreateTranscriptionRequestFile(
        content='\#BbTW\'zX9'.encode(),
        file='Buckinghamshire',
    ),
shared.CreateTranscriptionRequestModel2.WHISPER_1,
)

res = s.audio.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.CreateTranscriptionRequest](../../models/shared/createtranscriptionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateTranscriptionResponse](../../models/operations/createtranscriptionresponse.md)**


## create_translation

Translates audio into English.

### Example Usage

```python
import gpt
from gpt.models import shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateTranslationRequest(
    file=shared.CreateTranslationRequestFile(
        content='M57UL;W3rx'.encode(),
        file='Reggae Toys silver',
    ),
shared.CreateTranslationRequestModel2.WHISPER_1,
)

res = s.audio.create_translation(req)

if res.create_translation_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.CreateTranslationRequest](../../models/shared/createtranslationrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateTranslationResponse](../../models/operations/createtranslationresponse.md)**

