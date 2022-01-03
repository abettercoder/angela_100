# Step-1 : Guessing a letter from a word
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess_letter = input("Guess a letter: ").lower()

for letter in range(len(chosen_word)):
    if guess_letter == chosen_word[letter]:
        print("RIGHT")
    else:
        print("WRONG")