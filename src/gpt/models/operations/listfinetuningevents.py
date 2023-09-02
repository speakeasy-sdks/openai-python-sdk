"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listfinetuningjobeventsresponse as shared_listfinetuningjobeventsresponse
from typing import Optional



@dataclasses.dataclass
class ListFineTuningEventsRequest:
    fine_tuning_job_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'fine_tuning_job_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the fine-tuning job to get events for."""
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Identifier for the last event from the previous pagination request."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of events to retrieve."""
    




@dataclasses.dataclass
class ListFineTuningEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_fine_tuning_job_events_response: Optional[shared_listfinetuningjobeventsresponse.ListFineTuningJobEventsResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

