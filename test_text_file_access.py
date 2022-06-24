from FileAccess import *
from TextFileAccess import TextFileAccess


def test_open_read() -> str:
    """It should get file content"""
    file_name = "in1.txt"
    result = TextFileAccess.open_read(file_name)
    print(result)



test_open_read()