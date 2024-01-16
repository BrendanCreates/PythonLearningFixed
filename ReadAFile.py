try:
    with open("C:\\Users\\Brenb\\Desktop\\track.txt") as file:
        print(file.read()) # with will close file after opening it
except FileNotFoundError:
    print("That file was not found")
print(file.closed) # prints if the file is closed or not