import requests
from . import utils
from openai.models import operations, shared
from typing import Any, Optional

class OpenAI:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def cancel_fine_tune(self, request: operations.CancelFineTuneRequest) -> operations.CancelFineTuneResponse:
        r"""Immediately cancel a fine-tune job.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/fine-tunes/{fine_tune_id}/cancel", request.path_params)
        
        
        client = self._client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.CancelFineTuneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.fine_tune = out

        return res

    
    def create_answer(self, request: operations.CreateAnswerRequest) -> operations.CreateAnswerResponse:
        r"""Answers the specified question using the provided documents and examples.
        
        The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions).
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/answers"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateAnswerResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateAnswerResponse])
                res.create_answer_response = out

        return res

    
    def create_classification(self, request: operations.CreateClassificationRequest) -> operations.CreateClassificationResponse:
        r"""Classifies the specified `query` using provided examples.
        
        The endpoint first [searches](/docs/api-reference/searches) over the labeled examples
        to select the ones most relevant for the particular query. Then, the relevant examples
        are combined with the query to construct a prompt to produce the final label via the
        [completions](/docs/api-reference/completions) endpoint.
        
        Labeled examples can be provided via an uploaded `file`, or explicitly listed in the
        request using the `examples` parameter for quick tests and small scale use cases.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/classifications"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateClassificationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateClassificationResponse])
                res.create_classification_response = out

        return res

    
    def create_completion(self, request: operations.CreateCompletionRequest) -> operations.CreateCompletionResponse:
        r"""Creates a completion for the provided prompt and parameters
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/completions"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateCompletionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateCompletionResponse])
                res.create_completion_response = out

        return res

    
    def create_edit(self, request: operations.CreateEditRequest) -> operations.CreateEditResponse:
        r"""Creates a new edit for the provided input, instruction, and parameters
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/edits"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEditResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateEditResponse])
                res.create_edit_response = out

        return res

    
    def create_embedding(self, request: operations.CreateEmbeddingRequest) -> operations.CreateEmbeddingResponse:
        r"""Creates an embedding vector representing the input text.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/embeddings"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEmbeddingResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateEmbeddingResponse])
                res.create_embedding_response = out

        return res

    
    def create_file(self, request: operations.CreateFileRequest) -> operations.CreateFileResponse:
        r"""Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/files"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateFileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.open_ai_file = out

        return res

    
    def create_fine_tune(self, request: operations.CreateFineTuneRequest) -> operations.CreateFineTuneResponse:
        r"""Creates a job that fine-tunes a specified model from a given dataset.
        
        Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.
        
        [Learn more about Fine-tuning](/docs/guides/fine-tuning)
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/fine-tunes"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateFineTuneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.fine_tune = out

        return res

    
    def create_image(self, request: operations.CreateImageRequest) -> operations.CreateImageResponse:
        r"""Creates an image given a prompt.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/images/generations"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateImageResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.images_response = out

        return res

    
    def create_image_edit(self, request: operations.CreateImageEditRequest) -> operations.CreateImageEditResponse:
        r"""Creates an edited or extended image given an original image and a prompt.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/images/edits"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateImageEditResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.images_response = out

        return res

    
    def create_image_variation(self, request: operations.CreateImageVariationRequest) -> operations.CreateImageVariationResponse:
        r"""Creates a variation of a given image.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/images/variations"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateImageVariationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.images_response = out

        return res

    
    def create_moderation(self, request: operations.CreateModerationRequest) -> operations.CreateModerationResponse:
        r"""Classifies if text violates OpenAI's Content Policy
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/moderations"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateModerationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateModerationResponse])
                res.create_moderation_response = out

        return res

    
    def create_search(self, request: operations.CreateSearchRequest) -> operations.CreateSearchResponse:
        r"""The search endpoint computes similarity scores between provided query and documents. Documents can be passed directly to the API if there are no more than 200 of them.
        
        To go beyond the 200 document limit, documents can be processed offline and then used for efficient retrieval at query time. When `file` is set, the search endpoint searches over all the documents in the given file and returns up to the `max_rerank` number of documents. These documents will be returned along with their search scores.
        
        The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go higher), where a score above 200 usually means the document is semantically similar to the query.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/engines/{engine_id}/search", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateSearchResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateSearchResponse])
                res.create_search_response = out

        return res

    
    def delete_file(self, request: operations.DeleteFileRequest) -> operations.DeleteFileResponse:
        r"""Delete a file.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/files/{file_id}", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteFileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DeleteFileResponse])
                res.delete_file_response = out

        return res

    
    def delete_model(self, request: operations.DeleteModelRequest) -> operations.DeleteModelResponse:
        r"""Delete a fine-tuned model. You must have the Owner role in your organization.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/models/{model}", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DeleteModelResponse])
                res.delete_model_response = out

        return res

    
    def download_file(self, request: operations.DownloadFileRequest) -> operations.DownloadFileResponse:
        r"""Returns the contents of the specified file
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/files/{file_id}/content", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadFileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                res.download_file_200_application_json_string = r.content

        return res

    
    def list_engines(self) -> operations.ListEnginesResponse:
        r"""Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engines"
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListEnginesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListEnginesResponse])
                res.list_engines_response = out

        return res

    
    def list_files(self) -> operations.ListFilesResponse:
        r"""Returns a list of files that belong to the user's organization.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/files"
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListFilesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListFilesResponse])
                res.list_files_response = out

        return res

    
    def list_fine_tune_events(self, request: operations.ListFineTuneEventsRequest) -> operations.ListFineTuneEventsResponse:
        r"""Get fine-grained status updates for a fine-tune job.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/fine-tunes/{fine_tune_id}/events", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListFineTuneEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListFineTuneEventsResponse])
                res.list_fine_tune_events_response = out

        return res

    
    def list_fine_tunes(self) -> operations.ListFineTunesResponse:
        r"""List your organization's fine-tuning jobs
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/fine-tunes"
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListFineTunesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListFineTunesResponse])
                res.list_fine_tunes_response = out

        return res

    
    def list_models(self) -> operations.ListModelsResponse:
        r"""Lists the currently available models, and provides basic information about each one such as the owner and availability.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/models"
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListModelsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListModelsResponse])
                res.list_models_response = out

        return res

    
    def retrieve_engine(self, request: operations.RetrieveEngineRequest) -> operations.RetrieveEngineResponse:
        r"""Retrieves a model instance, providing basic information about it such as the owner and availability.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/engines/{engine_id}", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RetrieveEngineResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.engine = out

        return res

    
    def retrieve_file(self, request: operations.RetrieveFileRequest) -> operations.RetrieveFileResponse:
        r"""Returns information about a specific file.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/files/{file_id}", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RetrieveFileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.open_ai_file = out

        return res

    
    def retrieve_fine_tune(self, request: operations.RetrieveFineTuneRequest) -> operations.RetrieveFineTuneResponse:
        r"""Gets info about the fine-tune job.
        
        [Learn more about Fine-tuning](/docs/guides/fine-tuning)
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/fine-tunes/{fine_tune_id}", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RetrieveFineTuneResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.fine_tune = out

        return res

    
    def retrieve_model(self, request: operations.RetrieveModelRequest) -> operations.RetrieveModelResponse:
        r"""Retrieves a model instance, providing basic information about the model such as the owner and permissioning.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/models/{model}", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RetrieveModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.model = out

        return res

    