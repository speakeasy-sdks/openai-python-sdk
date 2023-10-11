<!-- Start SDK Example Usage -->


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
<!-- End SDK Example Usage -->