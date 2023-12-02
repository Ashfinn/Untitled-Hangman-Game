import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#print(f'Pssst, the solution is {chosen_word}.')

display = []

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

for _ in enumerate(chosen_word):
    display.append("_")

while True:
    guess = input("Guess a letter: ").lower()

    if guess.isalpha():
        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display[i] = guess
        else:
            lives -= 1
            print (f"You Lost a Life! You have {lives} lives remaining.")

        print(display)

        if display.count("_") == 0:
            print("YOU WIN!")
            break
        if lives == 0:
            print("YOU LOSE!")
            break
    else:
        print("INCORRECT INPUT! Please enter a letter.")



    #TODO-2: - If guess is not a letter in the chosen_word,

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.