from pandas import read_csv
from pandas.core.frame import DataFrame

from application.interface.infrastructure.data_schema_generator import IDataSchemaGenerator


class PandasDataSchemaGenerator(IDataSchemaGenerator):
    def get_data_schema(self, path_to_data: str) -> tuple[DataFrame, list[str]]:
        data_schema = []

        try:
            df = read_csv(path_to_data)
        except Exception as e:
            print(f'Произошла ошибка при чтении файла: {e}')
            return

        for column in df.columns:
            num_unique_values = df[column].nunique()

            if num_unique_values <= 15:
                data_schema.append(f'    Столбец с именем {column}, возможные значения - {list(df[column].unique())}\n')
            else:
                data_schema.append(f'    Столбец с именем {column}, тип данных - {df[column].dtype}\n')

        return df, data_schema
