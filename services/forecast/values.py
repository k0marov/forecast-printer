import dataclasses
import datetime


@dataclasses.dataclass
class WeatherCondition:
    text: str
    icon: str

@dataclasses.dataclass
class DayWeather:
    # date: datetime.date
    temp_c: float
    # wind_kmh: float
    # chance_of_rain: float
    # condition: WeatherCondition

@dataclasses.dataclass
class Forecast:
    today: DayWeather
    # tomorrow: DayWeather
