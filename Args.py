# *args - paramater that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args): # *args can be any name so long as there is an asterisk, asterisk is a form of packing into a tuple
    sum = 0
    args = list(args) # casting the tuple as a list because values in a tuple cannot be changed
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6)) # print(add(1,2,3)) gives an error because 3 positional arguments were given but add()
                              # only takes two
