# Tuple - collection is ordered and cant change
# good for collections of data that should not change, which protects from errors and is faster than lists

student = ("Bro",21,"male")

print(student.count("Bro")) # count the number of times the value of "Bro" appears in a tuple
print(student.index("male")) # prints the index of a value in a tuple

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")