import random
from collections import Counter
import re

# dictionary_words = []

# # read in the words
# with open('/usr/share/dict/words') as f:
#     for line in f:
#         dictionary_words = f.read().splitlines()

# # pick random words
# def pick_random_words(length):
#     words = random.sample(dictionary_words, length)
#     sentence = ' '.join(words)
#     return sentence
#print(pick_random_words(5))
#filename = 'test_text.txt'


def histogram(filename):
    with open(filename) as file:
        words = file.read().splitlines()
        # Remove '; , .' 
        sanitized_text = re.sub(r"[^a-zA-Z0-9 ]", "", ' '.join(words))

    # Added .lower() so that 'The' is the same as 'The' and both count for 'the'
    histogram = dict(Counter((sanitized_text.lower()).split()))  
    return histogram

def unique_words(histogram):
    total = 0
    for count in histogram.values():
        if count < 2:
          total += 1
    return total

def frequency(word, histogram):
    for entry, frequency in histogram.items():
        if entry == word:
            return frequency 


# new_histogram = histogram('../source_text.txt')
# total_unique_words = unique_words(new_histogram)

# print(new_histogram)
# print('total unique words: ', total_unique_words)
# print('Occurrence of the word THE is: ', frequency('the', new_histogram))



