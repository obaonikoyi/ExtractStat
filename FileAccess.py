from abc import ABC, abstractmethod



class FileAccess(ABC):

    @abstractmethod
    def open_read(file_name):
        pass

    @abstractmethod
    def open_write(file_name, write_text):
        pass




