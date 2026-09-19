"""src/config/config.py"""
from dotenv import load_dotenv

from pydantic import Field
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    jwt_key: str = Field(alias='JWT_KEY')
    jwt_alg: str = Field(alias='JWT_ALG')

load_dotenv()
cfg = Config()
