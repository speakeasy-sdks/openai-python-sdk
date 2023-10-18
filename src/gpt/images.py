"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from gpt import utils
from gpt.models import errors, operations, shared
from typing import Optional

class Images:
    r"""Given a prompt and/or an input image, the model will generate a new image."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_image(self, request: shared.CreateImageRequest) -> operations.CreateImageResponse:
        r"""Creates an image given a prompt."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/images/generations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def create_image_edit(self, request: shared.CreateImageEditRequest) -> operations.CreateImageEditResponse:
        r"""Creates an edited or extended image given an original image and a prompt."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/images/edits'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageEditResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def create_image_variation(self, request: shared.CreateImageVariationRequest) -> operations.CreateImageVariationResponse:
        r"""Creates a variation of a given image."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/images/variations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateImageVariationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ImagesResponse])
                res.images_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    