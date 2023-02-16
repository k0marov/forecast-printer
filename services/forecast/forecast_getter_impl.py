import dataclasses

from . import forecast_getter
import typing
import requests as requests
from . import values


_BASE_URL = "https://api.weatherapi.com/v1/forecast.json?q=Sochi&days=1&aqi=no&alerts=no"

@dataclasses.dataclass
class APIConfig:
    key: str

class APIForecastGetter(forecast_getter.ForecastGetter):
    def __init__(self, config: APIConfig):
        self.config = config
    def get_forecast(self) -> values.Forecast:
        return self._map_forecast(self._get_forecast_json())

    def _get_forecast_json(self) -> typing.Dict:
        url = _BASE_URL + "&key=" + self.config.api_key
        return requests.get(url).json()

    def _map_forecast(self, json: typing.Dict) -> values.Forecast:
        return values.Forecast(
            today=values.DayWeather(
                temp_c=json["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
            ),
        )
