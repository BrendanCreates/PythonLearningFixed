import os

source = "cheese.txt" # in my project folder so I do not need the directory info
destination = "C:\\Users\\Brenb\\Desktop\\cheese.txt" # \\ is the escape sequence to print a backslash in a string

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

new_source = "folder"
new_destination = "C:\\Users\\Brenb\\Desktop\\folder"

try:
    if os.path.exists(new_destination):
        print("There is already a file there")
    else:
        os.replace(new_source, new_destination)
        print(new_source+" was moved")
except FileNotFoundError:
    print(new_source+" was not found")