"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class CreateFileRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    




@dataclasses.dataclass
class CreateFileRequest:
    file: CreateFileRequestFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    r"""Name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
    
    If the `purpose` is set to \"fine-tune\", each line is a JSON record with \"prompt\" and \"completion\" fields representing your [training examples](/docs/guides/fine-tuning/prepare-training-data).
    """
    purpose: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'purpose' }})
    r"""The intended purpose of the uploaded documents.
    
    Use \"fine-tune\" for [Fine-tuning](/docs/api-reference/fine-tunes). This allows us to validate the format of the uploaded file.
    """
    

