# String Methods

name = "Brendan"

print(len(name))
print(name.find("B")) # index of character in string, if not found return -1
print(name.capitalize()) # only first letter in string not any other words
print(name.upper()) # all uppercase
print(name.lower()) # all lowercase
print(name.isdigit()) # if string is all numbers it returns true
print(name.isalpha()) # does it contain only letters, if has space it is false
print(name.count()) # count however many characters in string or how many of a character count("o")
print(name.replace("o", "a")) # replaces all of a certain character with another character
print(name*3)

