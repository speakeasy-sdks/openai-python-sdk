
import requests
from . import utils
from .openai import OpenAI

SERVERS = [
	"https://api.openai.com/v1",
]


class Openai:
    
    open_ai: OpenAI

    _client: requests.Session
    _security_client: requests.Session
    
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.0"
    _gen_version: str = "1.5.0"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        self._init_sdks()


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if params is not None:
            self._server_url = utils.replace_parameters(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    

    def config_client(self, client: requests.Session):
        self._client = client
        self._init_sdks()
    
    
    def _init_sdks(self):
        
        self.open_ai = OpenAI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
    
    