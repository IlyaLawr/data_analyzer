from abc import ABC, abstractmethod


class IClientLLM(ABC):
    @abstractmethod
    async def create_and_send_request(self, context: list[str]) -> str | None:
        """
        Отправляет запрос в LLM на основе переданного контекста.

        :param context: Список сообщений и ролей (строк), формирующих диалог.
        :return: Ответ модели в виде строки, либо None при ошибке/таймауте.
        """
        pass
