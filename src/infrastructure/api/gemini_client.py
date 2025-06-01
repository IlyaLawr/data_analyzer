from httpx import AsyncClient, Timeout, ReadTimeout, ConnectTimeout, WriteTimeout
from orjson import dumps

from infrastructure.api.gemini_builder import GeminiRequestDataBuilder
from infrastructure.api.gemini_parser import GeminiResponseParser


class GeminiAPIClient():
    def __init__(self,
                 url: str,
                 key: str,
                 proxy: str | None) -> None:
        self._url = url
        self._key = key
        
        client_kwargs = {
            'timeout': Timeout(15, read=50),
            'headers': {'Content-Type': 'application/json'}
        }
        if proxy:
            client_kwargs['proxy'] = proxy

        self._bulder = GeminiRequestDataBuilder()
        self._client = AsyncClient(**client_kwargs)
        self._parser = GeminiResponseParser()


    async def create_and_send_request(self, context: list[str]) -> str | None:
        payload_data = self._bulder.make_request_data(context)

        try:
            response = await self._client.post(f'{self._url}{self._key}', data=dumps(payload_data))
            if response.status_code == 200:
                return self._parser.parse(response.content)
        except (ReadTimeout, ConnectTimeout, WriteTimeout):
            return None
