import abc

from services.forecast import values


class ForecastGetter(abc.ABC):
    @abc.abstractmethod
    def get_forecast(self) -> values.Forecast:
        pass
