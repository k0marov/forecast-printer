import abc
import io

from services.forecast import values


class PDFConverter(abc.ABC):
    @abc.abstractmethod
    def save_pdf(self, forecast: values.Forecast) -> io.FileIO:
        """Save the forecast in a *temporary* pdf file that is deleted when the returned file object is closed"""
        pass