import random

dictionary_words = []

# read in the words
with open('/usr/share/dict/words') as f:
    for line in f:
        dictionary_words = f.read().splitlines()

# pick random words
def pick_random_words(length):
    words = random.sample(dictionary_words, length)
    sentence = ' '.join(words)
    return sentence


print(pick_random_words(5))