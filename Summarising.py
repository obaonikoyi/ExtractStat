
from ast import List
from collections import Counter


class Summarising:
    """
    The Summarising class is responsble for computing statistics about each file
    """
    
    # returns amount of element in the token
    def number_of_words(token: List[str]):
        return len(token)

    # gets the most frequent words in token and returns the word and its count in a List, tuple.
    def most_frequent_words(token: List[str], number_specified: int):
        count = Counter(token)
  
        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = count.most_common(number_specified)
        return(most_occur)
         
