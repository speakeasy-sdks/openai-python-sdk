"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import listrunstepsresponse as components_listrunstepsresponse
from enum import Enum
from typing import Optional

class ListRunStepsQueryParamOrder(str, Enum):
    r"""Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order."""
    ASC = 'asc'
    DESC = 'desc'


@dataclasses.dataclass
class ListRunStepsRequest:
    run_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'run_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the run the run steps belong to."""
    thread_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'thread_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the thread the run and run steps belong to."""
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list."""
    before: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    r"""A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list."""
    limit: Optional[int] = dataclasses.field(default=20, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20."""
    order: Optional[ListRunStepsQueryParamOrder] = dataclasses.field(default=ListRunStepsQueryParamOrder.DESC, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    r"""Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order."""
    



@dataclasses.dataclass
class ListRunStepsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_run_steps_response: Optional[components_listrunstepsresponse.ListRunStepsResponse] = dataclasses.field(default=None)
    r"""OK"""
    

