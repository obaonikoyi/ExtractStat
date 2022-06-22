

    
import os
from FileAccess import *
from Formatting import *
from Summarising import *
from Tokenising import *


class WordStatsManager:

    def print_summary(number_specified, output_spec, input_paths):
        for path in input_paths:
            file_cotent = TextFileAccess.get_file_content(path)
            token = StringTokenizer.split_text_to_token(file_cotent)
            number_of_words = SummaryStatistics.number_of_words(token)
            most_frequent_words = SummaryStatistics.most_frequent_words(token, number_specified)

            def get_format_from_path(path):
                _base, extension = os.path.splitext(path)
                return extension.lower()

            format = get_format_from_path(path)
            if format == '.csv' :
                text_result = CSVFileFormat.format_file_summary(path, number_of_words,most_frequent_words)
            else: 
                text_result = TextFileFormat.format_file_summary(path, number_of_words,most_frequent_words)

            TextFileAccess.open_write(text_result)
            print(text_result)
                   
