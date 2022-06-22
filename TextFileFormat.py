from FileFormat import Formatting


class TextFileFormat(FileFormat):

    def format_file_summary(input_file_name, number_of_words, most_frequent_words):
        line_count = 0

        write_text = "File" + input_file_name + "contains" + number_of_words + "words. Frequent words are: "
        for key, value in most_frequent_words.items():
            write_text += key + " (" + value + ")"
            if line_count == len(most_frequent_words):
                write_text += "."
            else:
                write_text += ","
        
        write_text += "\n"
        return write_text