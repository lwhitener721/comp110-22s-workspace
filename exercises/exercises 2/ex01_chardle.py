"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730479707"

five_character_word: str = input("Enter a  5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()
else:
    
    character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character. ")
    exit()
else:
    print("Searching for " + character + " in " + five_character_word)


if character == five_character_word[0]:
    print(str(character) + " found at index 0 ")
if character == five_character_word[1]:
    print(str(character) + " found at index 1 ")
if character == five_character_word[2]:
    print(str(character) + " found at index 2 ")
if character == five_character_word[3]:
    print(str(character) + " found at index 3 ")
if character == five_character_word[4]:
    print(str(character) + " found at index 4 ") 

letter_count = 0 
if character == five_character_word[0]:
    letter_count = letter_count + 1
if character == five_character_word[1]:
    letter_count = letter_count + 1
if character == five_character_word[2]:
    letter_count = letter_count + 1
if character == five_character_word[3]:
    letter_count = letter_count + 1
if character == five_character_word[4]:
    letter_count = letter_count + 1
if letter_count == 1:
    print(str(letter_count) + " instance of " + character + " found in " + str(five_character_word))
if letter_count == 0:
    print("No instances of " + character + " found in " + str(five_character_word))
if letter_count == 2:
    print(str(letter_count) + " instances of " + character + " found in " + str(five_character_word))
if letter_count == 3:
    print(str(letter_count) + " instances of " + character + " found in " + str(five_character_word))
if letter_count == 4:
    print(str(letter_count) + " instances of " + character + " found in " + str(five_character_word))
if letter_count == 5:
    print(str(letter_count) + " instances of " + character + " found in " + str(five_character_word))
