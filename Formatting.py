from abc import ABC, abstractmethod
from multiprocessing.sharedctypes import Value


class FileFormat(ABC):
    
    @abstractmethod
    def format_file_summary():
        pass

class TextFileFormat(FileFormat):
# [('a', 5), ('b', 4), ('c', 3), ('d', 2)]
    def format_file_summary(input_file_name, number_of_words, most_frequent_words):
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

class CSVFileFormat(FileFormat):

    def format_file_summary(input_file_name, number_of_words, most_frequent_words):
        line_count = 0
        write_csv = ""

        write_csv += input_file_name + "," + str(number_of_words)
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

