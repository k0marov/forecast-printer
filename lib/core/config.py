import os
import logging

import dotenv
from lib.features.forecast import forecast_getter_impl

class EnvKeys:
    FORECAST_API_KEY = 'FORECAST_API_KEY'

class Config:
    def __init__(self):
        dotenv.load_dotenv()

    def get_forecast_config(self) -> forecast_getter_impl.APIConfig:
        return forecast_getter_impl.APIConfig(self._get_from_env(EnvKeys.FORECAST_API_KEY))

    def _get_from_env(self, key: str) -> str:
        value = os.getenv(key)
        if value is None:
            logging.error(f"Could not find {key} environment variable!")
        return value
