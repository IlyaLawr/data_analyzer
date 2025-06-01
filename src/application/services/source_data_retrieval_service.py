from os import path, listdir
from kagglehub import dataset_download


class SourceDataRetrievalService:

    def get_path_to_data(self, dataset: str) -> str:
        dataset_path = dataset_download(dataset)

        files = listdir(dataset_path)
        filename = files[0]

        return path.join(dataset_path, filename)
