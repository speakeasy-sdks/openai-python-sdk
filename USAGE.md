<!-- Start SDK Example Usage -->
```python
import gpt
from gpt.models import operations, shared

s = gpt.Gpt()
   
req = operations.CancelFineTuneRequest(
    path_params=operations.CancelFineTunePathParams(
        fine_tune_id="unde",
    ),
)
    
res = s.open_ai.cancel_fine_tune(req)

if res.fine_tune is not None:
    # handle response
```
<!-- End SDK Example Usage -->