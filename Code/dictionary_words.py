import random
import numpy
from collections import Counter
import re
import sys

def create_histogram(filename):
    with open(filename) as file:
        words = file.read().splitlines()
        # Remove special char => '; , .'
        sanitized_text = re.sub(r"[^a-zA-Z0-9- ]", "", ' '.join(words))

    # 💡 - Counter (subclass of dict) goes through a list and return items and their frequency as a dict.
    histogram = dict(Counter((sanitized_text.lower()).split()))
    return histogram

# ! refactor below - must be a more efficient way to calculate entries of a dict -_-
def calculate_unique_words(histogram):
    total = 0
    for word in histogram.keys():
        total += 1
    return total

def calculate_frequency(word, histogram):
    for entry, frequency in histogram.items():
        if entry == word:
            return frequency

def pick_a_word(histogram, length):
    # 👇 equal weights
    # word = random.sample(list(histogram), length)
    # return word

    # 👇 different weights
    # total_unique_words = calculate_unique_words(histogram)
    total_words = 0

    # Get total words (NOT unique words)
    for frequency in histogram.values():
        total_words += frequency

    for word, frequency in histogram.items():
        histogram[word] = frequency/total_words

    print(histogram)

    selection = numpy.random.choice(list(histogram.keys()), length, p=list(histogram.values()))
    return selection

corpus = sys.argv[1]

new_histogram = create_histogram(corpus)

# print(new_histogram)
random_words = ' '.join(pick_a_word(new_histogram, 2))
print(random_words)

#! - source venv/bin/activate
