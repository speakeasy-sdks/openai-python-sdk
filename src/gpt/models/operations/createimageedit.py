"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import imagesresponse as shared_imagesresponse
from typing import Optional


@dataclasses.dataclass
class CreateImageEditResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    images_response: Optional[shared_imagesresponse.ImagesResponse] = dataclasses.field(default=None)

    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    