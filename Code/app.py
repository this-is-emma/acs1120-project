"""Main script, uses other modules to generate sentences."""
import random
import twitter
from flask import Flask, render_template, request, redirect

import sys
from markov_chain import generate_story, create_markov_model, clean_text

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
#! - source venv/bin/activate
# Any code placed here will run only once, when the server starts.
# corpus = sys.argv[1]
clean_corpus = clean_text('questions.txt')
mkv_model = create_markov_model(clean_corpus)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # return dictionary_words.random_words
    sentence = generate_story(
        mkv_model,
        limit = 6,
        start = random.choice([
            'would you',
            'you know',
            'you are',
            'when did',
            'if you',
            'do you',
            'is it',
        ])) + "?"
    return render_template('index.html', sentence = sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
