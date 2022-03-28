"""Examples of using lists in a simple game."""


from random import randint 


rolls: list[int] = list()

while len(rolls) == rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1,6))

#remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)

# sum the values of our rolls!
i: int = 0 
sum: int = 0 
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum} ")

#rolls: list[int] = list() 
#rolls.append(1)
#rolls.append(3)
#print(rolls[0])
#print(rolls[1])

#print(len(rolls))

#print(rolls[len(rolls) - 1])