import pytest

from lib.features.forecast.forecast_getter_impl import APIForecastGetter, APIConfig


def test_forecast_getter():
    forecast = APIForecastGetter(APIConfig(key="1234")).get_forecast()
    assert -100 <= forecast.today.temp_c <= 100