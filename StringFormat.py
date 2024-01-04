# str.format() - optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow","moon")) # curly brackets are placeholders called format fields
print("The {} jumped over the {}".format(animal,item)) # the first argument will go into the first format field
print("The {1} jumped over the {0}".format(animal,item)) # positional argument
print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Brendan"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name)) # left align (default)
print("Hello, my name is {:>10}. Nice to meet you.".format(name)) # right align
print("Hello, my name is {:^10}. Nice to meet you.".format(name)) # center align

number = 3.14159
nnumber = 1000

print("The number pi is {:.2f}".format(number)) # displays 3.14 and will round your number
print("The number is {:,}".format(nnumber)) # add comma to all thousands places
print("The number is {:b}".format(nnumber)) # binary
print("The number is {:o}".format(nnumber)) # octal
print("The number is {:x}".format(nnumber)) # hex
print("The number is {:e}".format(nnumber)) # scientific lowercase e
print("The number is {:E}".format(nnumber)) # scientific uppercase e