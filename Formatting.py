from abc import ABC, abstractmethod
from multiprocessing.sharedctypes import Value
 

class Formatting(ABC):
    
    @abstractmethod
    def format_file_summary(self, input_file_name: str, number_of_words: int, most_frequent_words: list[str]):
        pass

