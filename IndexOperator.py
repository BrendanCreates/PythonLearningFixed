# Index operator [] - give access to a sequence's elements (str,list,tuples)

name = "Brendan Nevils!"

if(name[0].isupper()):
    name = name.lower()

print(name)

first_name = name[:8].upper()
last_name = name[9:]
last_character = name[-1]

print(first_name)
print(last_name)