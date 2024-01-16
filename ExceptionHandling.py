# exception - an event detected during execution that disrupts the flow of the code
try: # basic form is surround dangerous code / user input in a try block
    numerator = int(input("Enter number"))
    denominator = int(input("Enter number"))
    result = numerator / denominator
except ZeroDivisionError as e: # you can define specific exceptions to catch and what to happen for specific exception
    print(e)
    print("You cannot divide by zero ya dummy")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e: # if exception occurs, the except block catches the exception, having this by itself isnt good
                  # practice
    print(e)
    print("Something went wrong")
# as e is standard practice
else:
    print(result)
finally: # no matte if there is an exception this block will always execute
    print("This will always execute")
