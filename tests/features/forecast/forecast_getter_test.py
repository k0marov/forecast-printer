import logging

from lib.core.config import Config
from lib.features.forecast.forecast_getter_impl import APIForecastGetter, APIConfig

def test_forecast_getter_smoke(config: Config):
    forecast = APIForecastGetter(config.get_forecast_config()).get_forecast()
    logging.info(f"Got forecast {forecast}")
    assert -100 <= forecast.today.temp_c <= 100