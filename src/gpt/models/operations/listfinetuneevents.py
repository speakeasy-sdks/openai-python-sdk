"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listfinetuneeventsresponse as shared_listfinetuneeventsresponse
from typing import Optional



@dataclasses.dataclass
class ListFineTuneEventsRequest:
    fine_tune_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tune_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the fine-tune job to get events for."""
    stream: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'stream', 'style': 'form', 'explode': True }})
    r"""Whether to stream events for the fine-tune job. If set to true,
    events will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available. The stream will terminate with a
    `data: [DONE]` message when the job is finished (succeeded, cancelled,
    or failed).

    If set to false, only events generated so far will be returned.
    """
    




@dataclasses.dataclass
class ListFineTuneEventsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_fine_tune_events_response: Optional[shared_listfinetuneeventsresponse.ListFineTuneEventsResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

