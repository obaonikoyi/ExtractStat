from abc import ABC, abstractmethod
from ast import List
from multiprocessing.sharedctypes import Value
 

class Formatting(ABC):
    
    @abstractmethod
    def format_file_summary(self, input_file_name, number_of_words, most_frequent_words):
        pass

class TextFormatting(Formatting):

    # returns file statistics in text format
    def format_file_summary(self, input_file_name: str, number_of_words: int, most_frequent_words: List[str]):
        line_count = 0
        write_text =""
        write_text += "File " + input_file_name + " contains " + str(number_of_words) + " words. Frequent words are:"
    
        for index, tuple in enumerate(most_frequent_words):
            line_count += 1
            element_one = tuple[0]
            element_two = tuple[1]
            write_text += " " + element_one + " (" + str(element_two) + ")"
            if line_count == len(most_frequent_words):
                write_text += "."
            else:
                write_text += ","
        
        write_text += "\n"
        return write_text

class CSVFormatting(Formatting):

    # returns file statistics in CSV format
    def format_file_summary(self, input_file_name, number_of_words, most_frequent_words):
        line_count = 0
        write_csv = ""

        write_csv += input_file_name + "," + str(number_of_words) + ","
        for index, tuple in enumerate(most_frequent_words):
            line_count += 1
            element_one = tuple[0]
            element_two = tuple[1]
            write_csv += element_one + "," + str(element_two)
            if line_count == len(most_frequent_words):
                write_csv += "."
            else:
                write_csv += ","
        
        write_csv += "\n"
        return write_csv


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
