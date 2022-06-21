
from collections import Counter


class SummaryStatistics:
    def number_of_words(token):
        return len(token)


    def most_frequent_words(token, number_specified):
        count = Counter(token)
  
        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = count.most_common(number_specified)
        return(most_occur)
         
