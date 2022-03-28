"""The functions for dictionary."""

__author__ = "730479707"


def invert(a_list: dict[str, str]) -> dict[str, str]:
    """Change keys to strings in function."""
    empty: dict[str, str] = {}
    for k in a_list:
        empty[a_list[k]] = k 
    return empty 


print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most frequent favorite color."""
    empty: dict[str, int] = {}
    favorite: str = ""
    i: int = 0
    for key in colors:
        if colors[key] in empty:
            empty[colors[key]] += 1
        else:
            empty[colors[key]] = 1
    for key in empty:
        if empty[key] > i:
            i = empty[key]
            favorite = key
    return favorite 
    

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))
        
    
def count(xs: list[str]) -> dict[str, int]:
    """List values in function is keys, while the number of times they appear are values."""
    empty = dict[str, int]() 
    for i in xs:
        if i in empty:
            empty[i] += 1
        else:
            empty[i] = 1
    return empty


print(count(["ha", "ha", "hahaha", "haha"]))