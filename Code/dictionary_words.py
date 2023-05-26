import random
from collections import Counter

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

# TODO remove special character either with regex as re.sub('[^A-Za-z0-9]+', '', mystring) OR with ''.join(e for e in string if e.isalnum())

def histogram(filename):
    with open(filename) as file: 
        for word in file:
            words = file.read().split()
    histogram = dict(Counter(words))  
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

new_histogram = histogram('test_text.txt')
total_unique_words = unique_words(new_histogram)

# print(total_unique_words)

print(frequency('the', new_histogram))