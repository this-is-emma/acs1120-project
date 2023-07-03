# ! BASED ON THIS YOUTUBE TUTORIAL :https://www.youtube.com/watch?v=E4WcBWuQQws&t=458s

import random
import re
import sys

def clean_text(filename):
    with open(filename) as file:
        words = file.read().splitlines()
        # Remove special char => '; , .'
        sanitized_text = re.sub(r"[^a-zA-Z0-9- ]", "", ' '.join(words))
        return (sanitized_text.lower()).split()

corpus = sys.argv[1]

clean_corpus = clean_text(corpus)
def create_markov_model(clean_text, n_gram=1):
    markov_model={}
    for i in range(len(clean_text) - n_gram - 1):
        curr_state, next_state = "", ""
        for j in range(n_gram):
            curr_state += clean_text[i+j] + " "
            next_state += clean_text[i+j+n_gram] + " "
        curr_state = curr_state[:-1]
        next_state = next_state[:-1]
        if curr_state not in markov_model:
            markov_model[curr_state] = {}
            markov_model[curr_state][next_state] = 1
        else:
            if next_state in markov_model[curr_state]:
                markov_model[curr_state][next_state] += 1
            else:
                markov_model[curr_state][next_state] = 1

    for curr_state, transition in markov_model.items():
        total = sum(transition.values())
        for state, count in transition.items():
            markov_model[curr_state][state] = count/total
        # print('Markov model is: ', markov_model)
        return markov_model

# start = random.choice(['what','why','when'])

def generate_story(markov_model, start, limit = 8):
    n=0
    curr_state = start
    next_state = None
    story = ""
    story += curr_state + " "
    while n < limit:
        next_state = random.choices(list(markov_model[curr_state].keys()), list(markov_model[curr_state].values()))
        curr_state = next_state[0]
        story += curr_state + " "
        n += 1

    return story

# mkv_model = create_markov_model(clean_corpus)
# # sentence = generate_story(mkv_model, start = random.choice(['what','why','when']))



