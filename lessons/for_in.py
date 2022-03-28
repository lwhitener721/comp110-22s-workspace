"""An example of for in syntax."""


names: list[str] = ["Kris", "Kyle", "Enzo", "marc" ] 

i: int = 0 
while i < len(names):
    name: str = names[i]
    print(names)
    i =+ 1


for name in names:
    print(names)