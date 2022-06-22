from FileAccess import *


def test_get_file_content() -> str:
    """It should get file content"""
    file_name = "in1.txt"
    result = TextFileAccess.get_file_content(file_name)
    print(result)



test_get_file_content()