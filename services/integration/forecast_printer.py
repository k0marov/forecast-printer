import abc


class ForecastPrinter(abc.ABC):
    @abc.abstractmethod
    def get_and_print_forecast(self) -> None:
        """Get the forecast, convert it to pdf and send it to the printer"""
        pass
