'''
1)Hangman Game:
Design a text-based Hangman game. The program
selects a random word, and the player guesses one
letter at a time to uncover the word. You can set a
limit on the number of incorrect guesses allowed.
'''


import random


def hangman():

    words = ["python", "developer", "hangman", "internship", "programming"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    max_attempts = 6
    attempts = 0
    guessed_letters = []

    print("Welcome to Hangman!")
    print("You have", max_attempts, "incorrect guesses allowed.")
    print("Word to guess: ", " ".join(guessed_word))

    while attempts < max_attempts:
        guess = input("\nGuess a letter: ").lower()


        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:

            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good job! The word now looks like this: ", " ".join(guessed_word))
        else:
            attempts += 1
            print("Wrong guess. You have", max_attempts - attempts, "guesses left.")

        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

hangman()
