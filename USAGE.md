<!-- Start SDK Example Usage [usage] -->
```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->