from re import search
from typing import Any

from pandas.core.frame import DataFrame

from application.interface.analyst import IAnalyst
from application.interface.infrastructure.client_llm import IClientLLM
from application.services.execute_code_service import ExecuteCodeService
from application.dataclasses import Context


class DataAnalyst(IAnalyst):
    def __init__(self, 
                 llm_client: IClientLLM,
                 code_executor: ExecuteCodeService,
                 context: Context):

        self._client = llm_client
        self._code_executor = code_executor
        self._context = context


    def set_data_schema(self, data: list[str]) -> None:
        self._context.set_message(f'Вот схема данных DataFrame - {''.join(data)}', 'user')


    async def process_question(self, question: str, df: DataFrame) -> str:
        self._context.set_message(f'Вопрос пользователя - {question}. Действуй строго согласно системной инструкции!', 'user')
        response_llm = await self._client.create_and_send_request(self._context.get_context())

        result = self._search_and_execution_code(response_llm, df)
        self._context.set_message(response_llm, 'model')

        self._context.set_message(
            f'Такой ответ сгенерировал твой код – {result}, '
            f'сформулируй структурированный и грамотный ответ на вопрос пользователя, '
            f'используя данные которые получились в результате исполнения твоего кода. '
            f'Нужен человекочитаемый ответ, код не требуется.',
            'user'
        )
        return await self._client.create_and_send_request(self._context.get_context())


    def _search_and_execution_code(self, response: str, df) -> Any:
        match = search(r'```python\s*([\s\S]*?)```', response)
        if match:
            code = match.group(1)
        return self._code_executor.execute(code, df)
