from infrastructure.api.utils import system_instruction


class GeminiRequestDataBuilder():

    @staticmethod
    def make_request_data(data: list[str]) -> dict:
        request_data = {}
        context = []

        values = iter(data)
        text, role = next(values, None), next(values, None)

        while text and role:
            context.append({'parts': [{'text': text}], 'role': role})
            text, role = next(values, None), next(values, None)
        
        if system_instruction:
            request_data['system_instruction'] = {'parts': { 'text': system_instruction}}

        request_data['contents'] = context
        return request_data
