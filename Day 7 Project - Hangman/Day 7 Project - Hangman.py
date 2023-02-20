import random
import hangmanWords
import hangmanArt

# It becomes false after the player run out of lives
still_alive = True

# Sets the amount of lives the player starts with
lives = 5

# Chooses a word from an imported list from the hangmanWords module
chosen_word = random.choice(hangmanWords.word_list)

# Gets the length of the chosen word, so it can be used on a loop later
word_length = len(chosen_word)

# Creates a list the size of the chosen word with blanks
display = []
for n in chosen_word:
    display += "_"

# Greets the player
print(f"Welcome to the HaNgMaN game 2000! You start the game with 5 lives.\nGuess the word -> {display}. The word is {chosen_word}")

#
while still_alive:
    # Asks the play for a letter
    guess = input("Choose a letter, any letter.")

    # chec
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = guess
    if guess not in chosen_word:
        lives -= 1
        print(hangmanArt.stages[lives])
        print(f"Wrong letter, try again. You have {lives} lives remaining.")

    if "_" not in display:
        still_alive = False
        print(f"You won. The word was {chosen_word}.")
        break
    if lives <= 0:
        still_alive = False
        print("Game over. You lost!")
        break

    print(display)

