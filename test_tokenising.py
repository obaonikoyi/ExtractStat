from Tokenising import *

def test_split_text_to_token():
    text = " a a a a a b b b b c c c d d e f g h i j kk kk"
    result = StringTokenizer.split_text_to_token(text)
    print(result)


test_split_text_to_token()
