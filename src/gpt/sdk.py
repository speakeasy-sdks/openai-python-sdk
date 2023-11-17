"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .assistant import Assistant
from .assistants import Assistants
from .audio import Audio
from .chat import Chat
from .completions import Completions
from .edits import Edits
from .embeddings import Embeddings
from .files import Files
from .fine_tunes import FineTunes
from .fine_tuning import FineTuning
from .images import Images
from .models_ import Models
from .moderations import Moderations
from .sdkconfiguration import SDKConfiguration
from gpt import utils
from gpt.models import components
from typing import Callable, Dict, Union

class Gpt:
    r"""OpenAI API: The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details."""
    assistants: Assistants
    r"""Build Assistants that can call models and use tools."""
    assistant: Assistant
    audio: Audio
    r"""Learn how to turn audio into text or text into audio."""
    chat: Chat
    r"""Given a list of messages comprising a conversation, the model will return a response."""
    completions: Completions
    r"""Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position."""
    edits: Edits
    r"""Given a prompt and an instruction, the model will return an edited version of the prompt."""
    embeddings: Embeddings
    r"""Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms."""
    files: Files
    r"""Files are used to upload documents that can be used with features like Assistants and Fine-tuning."""
    fine_tunes: FineTunes
    r"""Manage legacy fine-tuning jobs to tailor a model to your specific training data."""
    fine_tuning: FineTuning
    r"""Manage fine-tuning jobs to tailor a model to your specific training data."""
    images: Images
    r"""Given a prompt and/or an input image, the model will generate a new image."""
    models: Models
    r"""List and describe the various models available in the API."""
    moderations: Moderations
    r"""Given a input text, outputs if the model classifies it as violating OpenAI's content policy."""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key_auth: Union[str,Callable[[], str]],
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param api_key_auth: The api_key_auth required for authentication
        :type api_key_auth: Union[str,Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security = components.Security(api_key_auth = api_key_auth)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.assistants = Assistants(self.sdk_configuration)
        self.assistant = Assistant(self.sdk_configuration)
        self.audio = Audio(self.sdk_configuration)
        self.chat = Chat(self.sdk_configuration)
        self.completions = Completions(self.sdk_configuration)
        self.edits = Edits(self.sdk_configuration)
        self.embeddings = Embeddings(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.fine_tunes = FineTunes(self.sdk_configuration)
        self.fine_tuning = FineTuning(self.sdk_configuration)
        self.images = Images(self.sdk_configuration)
        self.models = Models(self.sdk_configuration)
        self.moderations = Moderations(self.sdk_configuration)
    