from abc import ABC, abstractmethod


class FileAccess(ABC):

    @abstractmethod
    def open_read(file_name):
        pass

    @abstractmethod
    def open_write(file_name, write_text):
        pass


class TextFileAccess(FileAccess):

    def get_file_content(file_name):
        with open(file_name, 'r') as file:
            return file.read() 

    def set_file_content(file_name, write_text):
        with open(file_name, 'w') as file:
            data = write_text
            file.write(data)


