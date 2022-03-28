"""Demonstrations of Dictionary capabilities."""

# declaring the type of dictionary 
schools = dict[str, int]

# initialize to an empty dictionary
schools = dict() 

# set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# PRINT A DICTIONARY LITERAL REPRESENTATion
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary by its key. 
schools.pop("Duke")

# Test for the existence of a key

if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200


# Demonstration of dictionary literals; empty dictionary literal
schools = {}  # same as dict()

# alternatively, initialize key-value pairs 
schools = {"UNC": 194000, "Duke": 6171, "NCSU": 26150}

# what happens when a key doesnt exists?
# print(schools["UNCC"])
# KeyError occurs 

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

# same loop output:
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")