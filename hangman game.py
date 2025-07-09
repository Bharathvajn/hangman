import random

# Predefined list of 5 words
word_list = ["apple", "brain", "chair", "dream", "eagle"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Display current word with underscores
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while attempts_left > 0:
    print(f"Word: {display_word()}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
    else:
        attempts_left -= 1
        print(f"Wrong guess! Attempts left: {attempts_left}\n")

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You guessed the word: {secret_word}")
        break
else:
    print(f"Game Over! The word was: {secret_word}")
