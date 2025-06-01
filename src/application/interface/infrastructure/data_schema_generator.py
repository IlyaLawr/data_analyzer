from abc import ABC, abstractmethod


class IDataSchemaGenerator(ABC):
    @abstractmethod
    def get_data_schema(self, path_to_data: str) -> list[str]:
        """
        Считывает файл по указанному пути и возвращает DataFrame вместе со «схемой» данных.

        :param path_to_data: Путь к CSV-файлу.
        :return: Кортеж (df, data_schema), где:
                 - df: pandas.DataFrame с загруженными данными.
                 - data_schema: список строк вида:
                   "Столбец {имя}, возможные значения – …" (если уникальных значений ≤ 15)
                   или
                   "Столбец {имя}, тип данных – {dtype}" (если уникальных значений > 15).
        """
        pass
