import random

x = random.randint(1,6) # random number between 1 - 6
print(x)
y = random.random() # random floating point number between 0 - 1
print(y)

myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)