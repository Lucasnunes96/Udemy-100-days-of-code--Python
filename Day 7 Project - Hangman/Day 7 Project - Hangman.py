import random
import hangmanWords
import hangmanArt

# It becomes false after the player run out of lives or wins
gameRunning = True

# Sets the amount of lives the player starts with
lives = 6

# Chooses a word from an imported list from the hangmanWords module
chosen_word = random.choice(hangmanWords.word_list)

# Gets the length of the chosen word, so it can be used on a loop later
word_length = len(chosen_word)

# Creates a list the size of the chosen word with blanks
display = []
for n in chosen_word:
    display += "_"

greetingDisplay = ",".join(display).replace(",", " ")

# Greets the player
print(f"Welcome to the HaNgMaN game 2000! You start the game with 6 lives.\nGuess the word -> {greetingDisplay} {chosen_word}.")

#
while gameRunning:
    # Asks the play for a letter
    guess = input("Choose a letter, any letter.")

    # check if the player's guess was correct or not. If it's not, then the player loses one life
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = guess
            print(hangmanArt.stages[lives])
    if guess not in chosen_word:
        lives -= 1

        # checks if the player ran out of lives
        if lives <= 0:
            gameRunning = False
            print(hangmanArt.stages[lives])
            print(f"Game over. You lost! The right word was {chosen_word}.")
            break
        else:
            print(hangmanArt.stages[lives])
            print(f"Wrong letter, try again. You have {lives} lives remaining.")

    # checks if the word is complete
    if "_" not in display:
        gameRunning = False
        print(f"You won. The word was {chosen_word}.")
        break

    print(",".join(display).replace(",", " "))

