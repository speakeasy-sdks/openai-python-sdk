<!-- Start SDK Example Usage -->


```python
import gpt
from gpt.models import operations

s = gpt.Gpt(
    api_key_auth="",
)


res = s.assistants.cancel_run(run_id='string', thread_id='string')

if res.run_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->