
class Tokenising:
    """
    The Tokenising class is responsible for turning any object to tokens
    """
    
    # The split_text_to_token() method breaks up a string at the specified separator and returns a list of strings.
    def split_text_to_token(text: str):
        token = text.split()
        return token
