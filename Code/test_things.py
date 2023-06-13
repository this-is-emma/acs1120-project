from dictogram import Dictogram

text = "SOME TESTsgjkbsk sfksdf testf afajh"

text_str = [['asa'], ['adfd']]

text_list = ['fgh','yes', 'box']
dictogram = Dictogram(text_list)
print(dictogram)
print(len(dictogram))

new_dict = dict(dictogram)
print(type(new_dict))
print(new_dict.keys())

