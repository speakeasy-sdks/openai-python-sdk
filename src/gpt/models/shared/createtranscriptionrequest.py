"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional



@dataclasses.dataclass
class CreateTranscriptionRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    




@dataclasses.dataclass
class CreateTranscriptionRequest:
    file: CreateTranscriptionRequestFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    r"""The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm."""
    model: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'model' }})
    r"""ID of the model to use. Only `whisper-1` is currently available."""
    language: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'language' }})
    r"""The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'prompt' }})
    r"""An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language."""
    response_format: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'response_format' }})
    r"""The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt."""
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'temperature' }})
    r"""The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit."""
    

