# Audio
(*.audio*)

## Overview

Learn how to turn audio into text or text into audio.

### Available Operations

* [create_speech](#create_speech) - Generates audio from the input text.
* [create_transcription](#create_transcription) - Transcribes audio into the input language.
* [create_translation](#create_translation) - Translates audio into English.

## create_speech

Generates audio from the input text.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateSpeechRequest(
    input='string',
components.CreateSpeechRequest2.TTS_1,
    voice=components.Voice.FABLE,
)

res = s.audio.create_speech(req)

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.CreateSpeechRequest](../../models/shared/createspeechrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateSpeechResponse](../../models/operations/createspeechresponse.md)**


## create_transcription

Transcribes audio into the input language.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateTranscriptionRequest(
    file=components.CreateTranscriptionRequestFile(
        content='0xe08fcc1Fd5'.encode(),
        file_name='buckinghamshire.gif',
    ),
components.CreateTranscriptionRequest2.WHISPER_1,
)

res = s.audio.create_transcription(req)

if res.create_transcription_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreateTranscriptionRequest](../../models/shared/createtranscriptionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateTranscriptionResponse](../../models/operations/createtranscriptionresponse.md)**


## create_translation

Translates audio into English.

### Example Usage

```python
import gpt
from gpt.models import components

s = gpt.Gpt(
    api_key_auth="",
)

req = components.CreateTranslationRequest(
    file=components.CreateTranslationRequestFile(
        content='0xa45ca6c4DE'.encode(),
        file_name='reggae_toys_silver.gif',
    ),
components.CreateTranslationRequest2.WHISPER_1,
)

res = s.audio.create_translation(req)

if res.create_translation_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateTranslationRequest](../../models/shared/createtranslationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateTranslationResponse](../../models/operations/createtranslationresponse.md)**

