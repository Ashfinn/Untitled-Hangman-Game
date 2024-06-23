let currentWord = '';
let displayedWord = '';
let attempts = 6;

const stages = [
    ` +---+
    |   |
        |
        |
        |
        |
  =========`,
    ` +---+
    |   |
    O   |
        |
        |
        |
  =========`,
    ` +---+
    |   |
    O   |
    |   |
        |
        |
  =========`,
    ` +---+
    |   |
    O   |
   /|   |
        |
        |
  =========`,
    ` +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========`,
    ` +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========`,
    ` +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========`
];

const logo = `
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _\` | '_ \\ / _\` | '_ \` _ \\ / _\` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    `;

document.getElementById('logo').innerText = logo;

window.onload = () => {
    fetch('/get_word')
        .then(response => response.json())
        .then(data => {
            currentWord = data.word;
            displayedWord = '_'.repeat(currentWord.length);
            document.getElementById('word-display').innerText = displayedWord;
            document.getElementById('hangman-art').innerText = stages[0];
        });
}

function makeGuess() {
    let guess = document.getElementById('guess-input').value;
    if (guess.length !== 1) {
        alert('Please enter a single letter');
        return;
    }

    let newDisplay = '';
    let found = false;
    for (let i = 0; i < currentWord.length; i++) {
        if (currentWord[i] === guess) {
            newDisplay += guess;
            found = true;
        } else {
            newDisplay += displayedWord[i];
        }
    }

    if (!found) {
        attempts--;
        document.getElementById('hangman-art').innerText = stages[stages.length - 1 - attempts];
        if (attempts === 0) {
            document.getElementById('message').innerText = 'Game Over!';
            document.getElementById('guess-input').disabled = true;
            return;
        }
    }

    displayedWord = newDisplay;
    document.getElementById('word-display').innerText = displayedWord;
    if (displayedWord === currentWord) {
        document.getElementById('message').innerText = 'You Won!';
    }

    document.getElementById('guess-input').value = '';
}
