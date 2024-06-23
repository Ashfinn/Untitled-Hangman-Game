from flask import Flask, render_template, jsonify
import random
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hangman_words as words

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    word = random.choice(words.word_list)
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(debug=True)