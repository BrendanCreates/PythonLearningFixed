# User Input

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # output is a string not int
height = float(input("How tall are you?: "))

age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + "cm tall")