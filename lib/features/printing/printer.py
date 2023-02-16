import abc


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self, pdf_path: str) -> None:
        """Print the pdf document provided as an argument to the default printer"""
        pass
