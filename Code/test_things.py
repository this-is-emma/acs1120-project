from dictogram import Dictogram


text_list = ['fgh','yes', 'box']
dictogram = Dictogram(text_list)

print(dictogram.get('peace', 0))

# dictogram.add_count('love', 2)
# print(dictogram.frequency('love'))
# print(dictogram)
# print(list(dictogram.keys()))
# print(dictogram.tokens)
# print(dictogram.types)
# print(dictogram.sample())

# word = ['a']

# print(word)
# word = ' '.join(word)
# print(word)
