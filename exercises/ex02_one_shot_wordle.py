"""Simplified version of wordle, in which the player has only one shot to guess the word."""

__author__ = "730409578"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# check that the user is inputting the correct guess length
while len(guess) != len(secret_word): 
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

i: int = 0
feedback: str = ""

# building the feedback string
while i < len(secret_word):
    # correct letter in the correct place
    if secret_word[i] == guess[i]:
        feedback = feedback + GREEN_BOX + " "
    else:
        i0: int = 0
        wrong_place: bool = False
        while i0 < len(secret_word):
            # the if statement will check each letter in the word to the letter of the guess
            # currently being evaluated and then if the letter is right, in the wrong place
            # it will change the bool recording whether or not that specific letter of guess
            # is in the word
            if secret_word[i0] == guess[i] and not wrong_place:
                wrong_place = True
            i0 = i0 + 1
        # these two parts of the then block are just reflecting if that guess letter was found 
        if wrong_place:
            feedback = feedback + YELLOW_BOX + " "
        else:
            feedback = feedback + WHITE_BOX + " "
    i = i + 1

print(feedback)


if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")