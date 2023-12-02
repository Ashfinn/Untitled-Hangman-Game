"""
    This code implements a simple hangman game.
"""
import random
import hangman_art as art
import hangman_words as words

chosen_word = random.choice(words.word_list)

display = []

lives = 6

for _ in enumerate(chosen_word):
    display.append("_")

print(art.logo)
print(display)

while True:
    guess = input("Guess a letter: ").lower()

    if guess.isalpha():
        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display[i] = guess
        else:
            lives -= 1
            print(art.stages[lives])

        print(display)

        if display.count("_") == 0:
            print("YOU WIN!")
            break
        if lives == 0:
            print("YOU LOSE!")
            break
    else:
        print("INCORRECT INPUT! Please enter a letter.")