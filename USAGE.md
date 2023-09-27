<!-- Start SDK Example Usage -->


```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CancelFineTuneRequest(
    fine_tune_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)

res = s.open_ai.cancel_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```
<!-- End SDK Example Usage -->