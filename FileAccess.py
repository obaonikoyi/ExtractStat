from abc import ABC, abstractmethod


class FileAccess(ABC):
    """
    FileAccess is an Abstract class or interface for acessing files
    """
    
    @abstractmethod
    def open_read(file_path: str):
        pass

    @abstractmethod
    def open_write(file_path: str, write_text: str):
        pass


