"""Testing dictionaries functions."""

__author__ = "730479707"


from dictionary import invert, count, favorite_color 


def test_favorite_color() -> None:
    """Testing if favorite_color returns correct string."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_again() -> None:
    """Testing if favorite_color returns correct string."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_thrice() -> None:
    """Testing if favorite_color returns correct string."""
    colors: dict[str, str] = {"Rider": "orange", "Tea": "orange", "Breaking": "orange"}
    assert favorite_color(colors) == "orange"


def test_invert() -> None:
    """Testing if invert returns dictrionary with keys and values flipped."""
    a_list: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a_list) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_again() -> None:
    """Testing if invert returns dictrionary with keys and values flipped."""
    a_list: dict[str, str] = {'ha': 'sucks', 'lol': 'i chuckled', 'lmao': 'dirt'}
    assert invert(a_list) == {'sucks': 'ha', 'i chuckled': 'lol', 'dirt': 'lmao'}


def test_invert_thrice() -> None:
    """Testing if invert returns dictrionary with keys and values flipped."""
    a_list: dict[str, str] = {}
    assert invert(a_list) == {}


def test_count() -> None:
    """Test to see if given a list, count returns a dictionary of the number of times a key appears."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_again() -> None:
    """Test to see if given a list, count returns a dictionary of the number of times a key appears."""
    xs: list[str] = ["he", "hehe", "he", "hehehe"]
    assert count(xs) == {'he': 2, 'hehe': 1, 'hehehe': 1}


def test_count_thrice() -> None:
    """Test to see if given a list, count returns a dictionary of the number of times a key appears."""
    xs: list[str] = ["grace", "aly", "meg", "sophia"]
    assert count(xs) == {'grace': 1, 'aly': 1, 'meg': 1, 'sophia': 1}
