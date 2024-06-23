from flask import Flask, render_template, jsonify
import random
import hangman_words as words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    word = random.choice(words.word_list)
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(debug=True)

# Vercel needs a callable named `app`
app = app