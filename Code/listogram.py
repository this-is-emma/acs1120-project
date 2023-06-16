#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random

def is_list_of_lists(obj):
    return isinstance(obj, list) and all(isinstance(sublist, list) for sublist in obj)

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            if is_list_of_lists(word_list):
                word_list = [item for sublist in word_list for item in sublist]
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # print('add count called!')
        if len(self) > 0:
            # print('List was NOT empty!')
            no_match = False
            for item in self:
                # print(f'word is {word} and we are looking at: {item[0]}')
                if item[0] == word:
                    no_match = False
                    # print(f'word: {word} matches item[0]: {item[0]}, increasing {item[1]} by 1. no_match is {no_match}')
                    item[1] += count
                    self.tokens += count
                    return
                elif item[0] != word:
                    no_match = True
                    # print(f'word: {word} does NOT matches item[0]: {item[0]}, no_match is {no_match}')
            # print('checking no match now')
            if no_match:
                # print(f'no match is {no_match}, adding {[word, count]} to {self}')
                self.append([word, count])
                self.tokens += count
        else:
            # print('List was empty!')
            self.append([word, count])
            # print(f'Adding {word}, self is now: {self}')
            self.tokens += count

        self.types = len(self)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        frequency = 0
        for items in self:
            if items[0] == word:
                frequency = items[1]

        return frequency

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for items in self:
            if items[0] == word:
                return True
            else:
                return False

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        match = False
        for items in self:
            if items[0] == target:
                match = True
                frequency = self.frequency(target)

        if match:
            return self.index([target, frequency])
        if not match:
            return None


    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        weights = []
        unique_words = []

        for tuples in self:
            unique_words.append(tuples[0])
            weights.append(tuples[1]/self.tokens)
        selection = random.choices(unique_words, weights)
        return selection


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
