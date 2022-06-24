from CSVFormatting import CSVFormatting
from Formatting import *
from TextFormatting import TextFormatting


def test_text_format_file_summary():
    input_file_name = "in1.txt"
    number_of_words = 22
    most_frequent_words = [('a', 5), ('b', 4), ('c', 3), ('d', 2)]
    test_text_formatting = TextFormatting()
    result = test_text_formatting.format_file_summary(input_file_name, number_of_words, most_frequent_words)
    print(result)

def test_csv_format_file_summary():
    input_file_name = "in1.txt"
    number_of_words = 22
    most_frequent_words = [('a', 5), ('b', 4), ('c', 3), ('d', 2)]
    test_csv_formatting = CSVFormatting()
    result = test_csv_formatting.format_file_summary(input_file_name, number_of_words, most_frequent_words)
    print(result)

test_text_format_file_summary()
test_csv_format_file_summary()