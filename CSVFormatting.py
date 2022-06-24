from Formatting import Formatting


class CSVFormatting(Formatting):

    def __init__(self) -> None:
        super().__init__()

    # returns file statistics in CSV format
    def format_file_summary(self, input_file_name: str, number_of_words: int, most_frequent_words: list[str]):
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
