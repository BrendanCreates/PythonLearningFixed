# Keyword arguments - arguments preceded by an identifier when we pass them to function
# the order of the arguments doesn't matter unlike positional arguments (typical ones)
# python knows the names of the arguments that our function receives

def crazy(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

crazy("Brendan", "Christopher", "Nevils") # Positional arguments
crazy(middle="Christopher", first="Brendan", last="Nevils") # Keyword arguments