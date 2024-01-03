# Scope - the region that a variable is recognized
# a variable is only available from inside the region that it is created
# global and locally scoped versions of a variable can be created

name = "Brendan"
def display_name():
    name = "Nevils"
    print(name)

print(name)

# global is available in and out of functions
# print(name) inside of a function is going to use local before global

# Order of variables used
# L - local
# E - enclosing
# G - global
# B - built-in