import random

words = ["some", "core", "lone", "bone"]
print(words)

# THIS METHOD MODIFIES THE ORIGINAL LIST
# def rearrange_words(input):
#     random.shuffle(input)
#     return input

#THIS ONE KEEPS THE ORIGINAL LIST INTACT
def rearrange_words(input):
    words = random.sample(input, len(input))
    return words
    

print(rearrange_words(words))