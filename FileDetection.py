import os

path = "C:\\Users\\Brenb\\Desktop\\track.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path): # could be a folder / directory
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location does not exist")