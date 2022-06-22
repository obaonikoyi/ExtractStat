from Summarising import *

def test_number_of_words():
    
    token = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'kk', 'kk']
    result = SummaryStatistics.number_of_words(token)
    print(result)

def test_most_frequent_words():
    
    token = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'kk', 'kk']
    number_specified = 4
    result = SummaryStatistics.most_frequent_words(token, number_specified)
    print(result)


test_number_of_words()
test_most_frequent_words()