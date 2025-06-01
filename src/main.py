import asyncio

from infrastructure.pandas_data_schema_generator import PandasDataSchemaGenerator
from infrastructure.api.gemini_client import GeminiAPIClient

from application.services.source_data_retrieval_service import SourceDataRetrievalService
from application.services.execute_code_service import ExecuteCodeService
from application.use_case.freelance_data_analysis import FreelanceDataAnalysis
from application.data_analyst import DataAnalyst
from application.dataclasses import Context

from presentation.cli import SetupCliParser

from settings import settings

client_api = GeminiAPIClient(url=settings.url,
                             key=settings.key,
                             proxy=settings.proxy,)

analyst = DataAnalyst(llm_client=client_api,
                      code_executor=ExecuteCodeService(),
                      context=Context())


frelance_data_analysis = FreelanceDataAnalysis(data_retrieval_service=SourceDataRetrievalService(),
                                               schema_generator=PandasDataSchemaGenerator(),
                                               data_analyst=analyst)


async def main():
    cli_parser = SetupCliParser('Processing the question.')
    args = cli_parser.parse()
    question = ' '.join(args.question)

    print(await frelance_data_analysis.analyze(question))


asyncio.run(main())
