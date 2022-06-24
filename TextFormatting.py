from Formatting import Formatting


class TextFormatting(Formatting):

    def __init__(self) -> None:
        super().__init__()
        

    # returns file statistics in text format
    def format_file_summary(self, input_file_name: str, number_of_words: int, most_frequent_words: list[str]):
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