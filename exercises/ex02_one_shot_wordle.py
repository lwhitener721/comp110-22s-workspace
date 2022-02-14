"""An attempt at Wordle."""
__author__ = "730479707"

secret = str("python")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
empty = str("")
i = int(0) 
exists_elsewhere: bool = False
j = int(0)


six_letter_guess: str = input("What is your 6-letter guess? ")


while len(six_letter_guess) != len(secret):
    six_letter_guess = input("That was not 6 letters! Try again: ")
while i < len(secret):
    if six_letter_guess[i] == secret[i]:
        empty = empty + GREEN_BOX
    else:
        exists_elsewhere = False
        j = 0
        while exists_elsewhere is not True and j < len(secret):
            if six_letter_guess[i] == secret[j]:
                exists_elsewhere = True  
            j = j + 1
        if exists_elsewhere is False:
            empty = empty + WHITE_BOX
        else:
            empty = empty + YELLOW_BOX
    i = i + 1
print(empty)
if six_letter_guess == secret: 
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")
