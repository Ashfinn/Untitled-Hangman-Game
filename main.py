import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in enumerate(chosen_word):
        display.append("_")

for i, letter in enumerate(chosen_word):
    if letter == guess:
        display[i] = guess

blanks = len(chosen_word)

for elem in display:
    if elem != "_":
        blanks -= 1


while True:
    guess = input("Guess a letter: ").lower()


print(display)


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.