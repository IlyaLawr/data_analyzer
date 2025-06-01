from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):

    url: str = Field(env='URL')
    key: str = Field(env='KEY')
    proxy: str = Field(env='PROXY')

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
