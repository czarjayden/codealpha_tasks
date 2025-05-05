import random

def hangman():
    words = ['tuples', 'hangman', 'programming', 'dictionary', 'phantom']
    word = random.choice(words)  # Randomly choose a word
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to the Hangman game!")
    print(f"The word has {len(word)} letters: {' '.join(guessed_word)}")

    while attempts > 0 and '_' in guessed_word:
        print(f"\nAttempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        print("Current word:", ' '.join(guessed_word))

    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()