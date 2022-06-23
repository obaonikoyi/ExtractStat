from distutils import text_file
import os
from FileAccess import *
from Formatting import *
from Summarising import *
from Tokenising import *


class WordStatsManager:
    """
    The WordStatsManager class orchestrates the use case process (reading, tokenising, summarising, formatting, outputting) 
    """

    # process text files, compute statistics about each file, and produce output in several different formats
    def process_file_statistiic(number_specified, output_spec, input_paths):
        for output in output_spec:

            for path in input_paths:
                
                file_cotent = TextFileAccess.open_read(path)
                token = Tokenising.split_text_to_token(file_cotent)
                number_of_words = Summarising.number_of_words(token)
                most_frequent_words = Summarising.most_frequent_words(token, number_specified)
                

                # get format from path
                format = get_format_from_path(output)
                print(format)
                result =""
                # If format of file is csv, return summary in csv format
                if format == '.csv' :
                    context = FormattingContext(CSVFormatting())
                    result = context.do_summary(path, number_of_words, most_frequent_words)

                # If format of file is txt, return summary in text format
                if format == '.txt' : 
                    context = FormattingContext(TextFormatting())
                    result = context.do_summary(path, number_of_words, most_frequent_words)


                TextFileAccess.open_write(output, result)
                print(result)


def get_format_from_path(path):
        _base, extension = os.path.splitext(path)
        return extension.lower()
