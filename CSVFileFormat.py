from FileFormat import Formatting


class CSVFileFormat(FileFormat):

    def format_file_summary(input_file_name, number_of_words, most_frequent_words):
        line_count = 0

        write_csv = input_file_name + "," + number_of_words + ","
        for key, value in most_frequent_words.items():
            write_csv += key + "," + value
            if line_count == len(most_frequent_words):
                write_csv += "."
            else:
                write_csv += ","
        
        write_csv += "\n"
        return write_csv