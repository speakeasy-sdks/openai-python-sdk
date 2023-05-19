"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from gpt.models import operations, shared
from typing import Optional

class OpenAI:
    r"""The OpenAI REST API"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def cancel_fine_tune(self, request: operations.CancelFineTuneRequest) -> operations.CancelFineTuneResponse:
        r"""Immediately cancel a fine-tune job."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.CancelFineTuneRequest, base_url, '/fine-tunes/{fine_tune_id}/cancel', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CancelFineTuneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FineTune])
                res.fine_tune = out

        return res

    
    def create_answer(self, request: shared.CreateAnswerRequest) -> operations.CreateAnswerResponse:
        r"""Answers the specified question using the provided documents and examples.
        
        The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions).
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/answers'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAnswerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateAnswerResponse])
                res.create_answer_response = out

        return res

    
    def create_chat_completion(self, request: shared.CreateChatCompletionRequest) -> operations.CreateChatCompletionResponse:
        r"""Creates a completion for the chat message"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/chat/completions'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateChatCompletionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateChatCompletionResponse])
                res.create_chat_completion_response = out

        return res

    
    def create_classification(self, request: shared.CreateClassificationRequest) -> operations.CreateClassificationResponse:
        r"""Classifies the specified `query` using provided examples.
        
        The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
        to select the ones most relevant for the particular query. Then, the relevant examples
        are combined with the query to construct a prompt to produce the final label via the
        [completions](/docs/api-reference/completions) endpoint.
        
        Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
        request using the `examples` parameter for quick tests and small scale use cases.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/classifications'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateClassificationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateClassificationResponse])
                res.create_classification_response = out

        return res

    
    def create_completion(self, request: shared.CreateCompletionRequest) -> operations.CreateCompletionResponse:
        r"""Creates a completion for the provided prompt and parameters"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/completions'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateCompletionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateCompletionResponse])
                res.create_completion_response = out

        return res

    
    def create_edit(self, request: shared.CreateEditRequest) -> operations.CreateEditResponse:
        r"""Creates a new edit for the provided input, instruction, and parameters."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/edits'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateEditResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateEditResponse])
                res.create_edit_response = out

        return res

    
    def create_embedding(self, request: shared.CreateEmbeddingRequest) -> operations.CreateEmbeddingResponse:
        r"""Creates an embedding vector representing the input text."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/embeddings'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateEmbeddingResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateEmbeddingResponse])
                res.create_embedding_response = out

        return res

    
    def create_file(self, request: shared.CreateFileRequest) -> operations.CreateFileResponse:
        r"""Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/files'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OpenAIFile])
                res.open_ai_file = out

        return res

    
    def create_fine_tune(self, request: shared.CreateFineTuneRequest) -> operations.CreateFineTuneResponse:
        r"""Creates a job that fine-tunes a specified model from a given dataset.
        
        Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.
        
        [Learn more about Fine-tuning](/docs/guides/fine-tuning)
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/fine-tunes'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateFineTuneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FineTune])
                res.fine_tune = out

        return res

    
    def create_image(self, request: shared.CreateImageRequest) -> operations.CreateImageResponse:
        r"""Creates an image given a prompt."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/images/generations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out

        return res

    
    def create_image_edit(self, request: shared.CreateImageEditRequest) -> operations.CreateImageEditResponse:
        r"""Creates an edited or extended image given an original image and a prompt."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/images/edits'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageEditResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out

        return res

    
    def create_image_variation(self, request: shared.CreateImageVariationRequest) -> operations.CreateImageVariationResponse:
        r"""Creates a variation of a given image."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/images/variations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageVariationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out

        return res

    
    def create_moderation(self, request: shared.CreateModerationRequest) -> operations.CreateModerationResponse:
        r"""Classifies if text violates OpenAI's Content Policy"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/moderations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateModerationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateModerationResponse])
                res.create_moderation_response = out

        return res

    
    def create_search(self, request: operations.CreateSearchRequest) -> operations.CreateSearchResponse:
        r"""The search endpoint computes similarity scores between provided query and documents. Documents can be passed directly to the API if there are no more than 200 of them.
        
        To go beyond the 200 document limit, documents can be processed offline and then used for efficient retrieval at query time. When `file` is set, the search endpoint searches over all the documents in the given file and returns up to the `max_rerank` number of documents. These documents will be returned along with their search scores.
        
        The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go higher), where a score above 200 usually means the document is semantically similar to the query.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateSearchRequest, base_url, '/engines/{engine_id}/search', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_search_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSearchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateSearchResponse])
                res.create_search_response = out

        return res

    
    def create_transcription(self, request: shared.CreateTranscriptionRequest) -> operations.CreateTranscriptionResponse:
        r"""Transcribes audio into the input language."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/audio/transcriptions'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateTranscriptionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateTranscriptionResponse])
                res.create_transcription_response = out

        return res

    
    def create_translation(self, request: shared.CreateTranslationRequest) -> operations.CreateTranslationResponse:
        r"""Translates audio into into English."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/audio/translations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateTranslationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateTranslationResponse])
                res.create_translation_response = out

        return res

    
    def delete_file(self, request: operations.DeleteFileRequest) -> operations.DeleteFileResponse:
        r"""Delete a file."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteFileRequest, base_url, '/files/{file_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteFileResponse])
                res.delete_file_response = out

        return res

    
    def delete_model(self, request: operations.DeleteModelRequest) -> operations.DeleteModelResponse:
        r"""Delete a fine-tuned model. You must have the Owner role in your organization."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteModelRequest, base_url, '/models/{model}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeleteModelResponse])
                res.delete_model_response = out

        return res

    
    def download_file(self, request: operations.DownloadFileRequest) -> operations.DownloadFileResponse:
        r"""Returns the contents of the specified file"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadFileRequest, base_url, '/files/{file_id}/content', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.download_file_200_application_json_string = http_res.content

        return res

    
    def list_engines(self) -> operations.ListEnginesResponse:
        r"""Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/engines'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListEnginesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListEnginesResponse])
                res.list_engines_response = out

        return res

    
    def list_files(self) -> operations.ListFilesResponse:
        r"""Returns a list of files that belong to the user's organization."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/files'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListFilesResponse])
                res.list_files_response = out

        return res

    
    def list_fine_tune_events(self, request: operations.ListFineTuneEventsRequest) -> operations.ListFineTuneEventsResponse:
        r"""Get fine-grained status updates for a fine-tune job."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListFineTuneEventsRequest, base_url, '/fine-tunes/{fine_tune_id}/events', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListFineTuneEventsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFineTuneEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListFineTuneEventsResponse])
                res.list_fine_tune_events_response = out

        return res

    
    def list_fine_tunes(self) -> operations.ListFineTunesResponse:
        r"""List your organization's fine-tuning jobs"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/fine-tunes'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFineTunesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListFineTunesResponse])
                res.list_fine_tunes_response = out

        return res

    
    def list_models(self) -> operations.ListModelsResponse:
        r"""Lists the currently available models, and provides basic information about each one such as the owner and availability."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/models'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListModelsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListModelsResponse])
                res.list_models_response = out

        return res

    
    def retrieve_engine(self, request: operations.RetrieveEngineRequest) -> operations.RetrieveEngineResponse:
        r"""Retrieves a model instance, providing basic information about it such as the owner and availability.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetrieveEngineRequest, base_url, '/engines/{engine_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetrieveEngineResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Engine])
                res.engine = out

        return res

    
    def retrieve_file(self, request: operations.RetrieveFileRequest) -> operations.RetrieveFileResponse:
        r"""Returns information about a specific file."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetrieveFileRequest, base_url, '/files/{file_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetrieveFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OpenAIFile])
                res.open_ai_file = out

        return res

    
    def retrieve_fine_tune(self, request: operations.RetrieveFineTuneRequest) -> operations.RetrieveFineTuneResponse:
        r"""Gets info about the fine-tune job.
        
        [Learn more about Fine-tuning](/docs/guides/fine-tuning)
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetrieveFineTuneRequest, base_url, '/fine-tunes/{fine_tune_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetrieveFineTuneResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FineTune])
                res.fine_tune = out

        return res

    
    def retrieve_model(self, request: operations.RetrieveModelRequest) -> operations.RetrieveModelResponse:
        r"""Retrieves a model instance, providing basic information about the model such as the owner and permissioning."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.RetrieveModelRequest, base_url, '/models/{model}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RetrieveModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Model])
                res.model = out

        return res

    