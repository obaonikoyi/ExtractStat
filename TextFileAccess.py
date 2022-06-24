from FileAccess import FileAccess


class TextFileAccess(FileAccess):
    """
    TextFileAccess class is used to access the '.txt' file 
    """
    
    # returns file content
    def open_read(file_path: str):
        with open(file_path, 'r') as file:
            return file.read() 

    # Appends text to file
    def open_write(file_path: str, write_text: str):
        with open(file_path, 'a') as file:
            data = write_text
            file.write(data)

