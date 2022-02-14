"""Wow, its actually Wordle."""
__author__ = "730479707"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """Prints if the single letter is found in other parameter."""
    i = int(0)
    assert len(letter) == 1  
    while i < len(word):
        if word[i] == letter:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Prints emoji that correseponds with whether the guess equals the secret."""
    empty: str = ""
    i = int(0) 
    assert len(guess) == len(secret)
    assert len(secret) == len(guess)
    while i < len(guess):
        if contains_char(guess[i], secret[i]):
            empty = empty + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                empty = empty + YELLOW_BOX
            else:
                empty = empty + WHITE_BOX
        i = i + 1 
    return empty


def input_guess(number: int) -> str:
    """Given a integer of expected length, prompt user."""
    guess: str = input(f"Enter a {number} character word: ")
    while len(guess) != number:
        guess = input(f"That wasn't {number} chars! Try Again: ")
    return guess 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 0
    playing: bool = True
    while turn < 6 and playing is True:
        turn = turn + 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            playing = False 
        
    if playing is False: 
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()