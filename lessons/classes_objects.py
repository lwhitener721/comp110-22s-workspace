"""Example of a class and object instantiation."""


class Pizza:
    """Models the ideas of a Pizza."""

    # Attribution Defitions
    size: str
    toppings: int
    extra_cheese: bool



def price(pizza: Pizza) -> float:
    """Calculate the price of pizza."""
    total: float = 0.0
    if pizza.size == "large":
        total += 10.0
    else:
        total += 8.0

    total += pizza.toppings * 0.75

    if pizza.extra_cheese:
        total += 1.0

    return total 


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False 

print(Pizza)
print(a_pizza)
print(a_pizza.size)

def __init__(self, size: str, toppings: int, extra_cheese: bool):
    """Constructor definition for initialization of attributes. """
    self.size = size
    self.toppings = toppings
    self.extra_cheese = extra_cheese

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)