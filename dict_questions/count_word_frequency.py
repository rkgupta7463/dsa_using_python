'''
Count Word Frequency

Define a function to count the frequency of words in a given list of words.

Example:

    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
    count_word_frequency(words) 

Output:

     {'apple': 3, 'orange': 2, 'banana': 1}
'''

#Using collections.Counter (short & pythonic)

from collections import Counter

def count_word_frequency(words):
    return dict(Counter(words))


# Example
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))


#Without Counter (manual dictionary)
def count_word_frequency(words):
    # TODO
    cwf={}
    for word in words:
        cwf[word]=cwf.get(word,0) + 1

    return cwf

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words) )