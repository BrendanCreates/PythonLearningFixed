# Loop control statements - change a loops execution from its normal sequence

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "240-495-3004"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print()

for i in range(1,21):
    if i == 13:
        pass # this is passive, doesnt force next iteration, continue does
    else:
        print(i)
