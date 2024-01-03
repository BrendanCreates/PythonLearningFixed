# **kwargs - parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs): # kwargs - key word arguments, the name can be anything but need **
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


hello(first="Brendan", middle="Christopher", last="Nevils")