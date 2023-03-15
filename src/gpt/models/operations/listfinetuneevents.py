from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listfinetuneeventsresponse as shared_listfinetuneeventsresponse
from typing import Optional


@dataclasses.dataclass
class ListFineTuneEventsRequest:
    fine_tune_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tune_id', 'style': 'simple', 'explode': False }})
    stream: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'stream', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListFineTuneEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_fine_tune_events_response: Optional[shared_listfinetuneeventsresponse.ListFineTuneEventsResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    