"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you into the secret club...")
    else:
        print("Go back to Davis")

# Define a function named contains
#    Parameters:
#        1. needle - the str we're searching for
#         2. haystack - the list of str values we're searching through 


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


print(__name__)

if __name__ == "__main__":
    main()
# algorithim: for each itme in haystack
# test if equal to needle 
# if so return true
# contains("Kevin Bacon", ["Kanye West, "Kevin Bacon"])
# would return strue 