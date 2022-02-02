"""Full wordle game, structured with in-module functions."""

__author__ = "730409578"


def contains_char(secret_word: str, check_letter: str) -> bool:
    """This function uses a while loop to check each letter of the secret_word argument against the check_letter argument. If the check_letter is present in the secret_word, it returns True."""
    assert len(check_letter) == 1
    i: int = 0
    letter_present: bool = False
    while i < len(secret_word):
        if check_letter == secret_word[i]:
            letter_present = True
        i += 1
    return letter_present


def emojified(guess: str, secret: str) -> str:
    """This function will compare the string secret to the string guess, adding a green box if the letters match, a yellow box if the current letter of guess is present in secret but not in that exact place, and a white box if the letter is not present at all."""
    assert len(secret) == len(guess)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_code: str = ""
    i: int = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            emoji_code += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_code += YELLOW_BOX
        else:
            emoji_code += WHITE_BOX
        i += 1
    return emoji_code


def input_guess(expected_length: int) -> str:
    """Receives the player's guess."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length: 
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    user_guess: str = ""
    has_won: bool = False
    while not has_won and turn <= 6:
        print(f"=== Turn {str(turn)}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {str(turn)}/6 turns!")
            has_won = True
        else:
            turn += 1
    if not has_won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()