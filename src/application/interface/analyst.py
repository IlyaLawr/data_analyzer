from abc import ABC, abstractmethod


class IAnalyst(ABC):
    @abstractmethod
    def set_data_schema(self, data: list[str]) -> None:
        """
        Устанавливает схему данных, которая будет использоваться для построения контекста запроса.

        :param data: Список строк, каждая из которых описывает один столбец в DataFrame.
        """
        pass


    @abstractmethod
    def process_question(self, question: str) -> str:
        """
        Обрабатывает вопрос пользователя, взаимодействует с LLM, выполняет сгенерированный код
        и возвращает финальный человекочитаемый ответ.

        :param question: Вопрос пользователя.
        :param df: DataFrame с данными, передаваемый в код для анализа.
        :return: Ответ модели в виде текста.
        """
        pass
