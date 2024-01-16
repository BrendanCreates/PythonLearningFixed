text = ("Yooooo\nThis is some text\nHave a good one")

with open("C:\\Users\\Brenb\\Desktop\\track.txt", "a") as file: # default is "r" for read, "w" for write, "a" append
    file.write(text) # this will overwrite the file