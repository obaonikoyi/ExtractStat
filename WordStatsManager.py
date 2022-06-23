from distutils import text_file
import os
from FileAccess import *
from Formatting import *
from Summarising import *
from Tokenising import *


class WordStatsManager:

    def print_summary(number_specified, output_spec, input_paths):
        for output in output_spec:

            for path in input_paths:
                
                file_cotent = TextFileAccess.open_read(path)
                token = StringTokenizer.split_text_to_token(file_cotent)
                number_of_words = SummaryStatistics.number_of_words(token)
                most_frequent_words = SummaryStatistics.most_frequent_words(token, number_specified)
                

                """ get format from path"""
                format = get_format_from_path(output)
                print(format)
                result =""
                # If format of file is csv, return summary in csv format
                if format == '.csv' :
                    context = FileFormatContext(CSVFileFormat())
                    result = context.do_summary(path, number_of_words, most_frequent_words)

                # If format of file is txt, return summary in text format
                if format == '.txt' : 
                    context = FileFormatContext(TextFileFormat())
                    result = context.do_summary(path, number_of_words, most_frequent_words)


                TextFileAccess.open_write(output, result)
                print(result)


def get_format_from_path(path):
        _base, extension = os.path.splitext(path)
        return extension.lower()
