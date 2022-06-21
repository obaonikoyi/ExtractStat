from abc import ABC, abstractmethod


class FileFormat(ABC):
    
    @abstractmethod
    def format_file_summary():
        pass

