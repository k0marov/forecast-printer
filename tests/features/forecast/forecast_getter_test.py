from lib.core.config import Config
from lib.features.forecast.forecast_getter_impl import APIForecastGetter, APIConfig

def test_forecast_getter():
    config = Config()
    api_config = config.get_forecast_config()
    forecast = APIForecastGetter(api_config).get_forecast()
    assert -100 <= forecast.today.temp_c <= 100