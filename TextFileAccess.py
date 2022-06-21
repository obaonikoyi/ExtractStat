from FileAccess import FileAccess


class TextFileAccess(FileAccess):

    def open_read(file_name):
        with open(file_name, 'r') as file:
            return file.read() 

    def open_write(file_name, write_text):
        with open(file_name, 'w') as file:
            data = write_text
            file.write(data)

