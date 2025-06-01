from application.interface.infrastructure.data_schema_generator import IDataSchemaGenerator
from application.interface.analyst import IAnalyst

from application.services.source_data_retrieval_service import SourceDataRetrievalService


class FreelanceDataAnalysis:
    def __init__(self,
                 data_retrieval_service: SourceDataRetrievalService,
                 schema_generator: IDataSchemaGenerator,
                 data_analyst: IAnalyst) -> None:

        self._data_retrieval_service = data_retrieval_service
        self._schema_generator = schema_generator
        self._data_analyst = data_analyst


    async def analyze(self, question: str) -> str:
        path = self._data_retrieval_service.get_path_to_data('shohinurpervezshohan/freelancer-earnings-and-job-trends')
        dataframe, data_schema =  self._schema_generator.get_data_schema(path)
        self._data_analyst.set_data_schema(data_schema)
        answer = await self._data_analyst.process_question(question, dataframe)
        return answer
