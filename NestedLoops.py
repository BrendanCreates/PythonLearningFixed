# Nested loops

rows = input("How many rows?: ")
columns = input("How many columns?: ")
symbol = input("What symbol would you like to use?: ")

for i in range(int(rows)):
    print(symbol*int(columns))

print()

for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end="") # prevents the cursor from going to the next line after printing
    print()