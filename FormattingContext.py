
from Formatting import Formatting


class FormattingContext():
    """
    The FormattingContext defines the interface of interest to clients.
    """

    def __init__(self, file_format: Formatting) -> None:
        """
        Usually, the FormattingContext accepts a file format through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._file_format = file_format

    @property
    def file_format(self) -> Formatting:
        """
        The FormattingContext maintains a reference to one of the Formatting objects. The
        Context does not know the concrete class of a file format. It should work
        with all strategies via the Strategy interface.
        """

        return self._file_format

    @file_format.setter
    def file_format(self, file_format: Formatting) -> None:
        """
        Usually, the FormattingContext allows replacing a Formatting object at runtime.
        """

        self._file_format = file_format

    def do_summary(self, input_file_name, number_of_words, most_frequent_words) -> str:
        """
        The FormattingContext delegates some work to the Formatting object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        
        result = self._file_format.format_file_summary(input_file_name, number_of_words, most_frequent_words)
        return result
