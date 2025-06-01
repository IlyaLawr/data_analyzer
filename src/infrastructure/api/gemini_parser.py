from orjson import loads, JSONDecodeError


class GeminiResponseParser():
    @staticmethod
    def parse(response: bytes) -> str:
        try:
            data = loads(response)
            return data['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, JSONDecodeError):
            return ''
