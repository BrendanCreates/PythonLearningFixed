# String Slicing
# to slice use indexing[] or slice()
# [start:stop:step]

name = "Brendan Nevils"

first_name = name[0] # B
print(first_name)
first_name = name[0:8] # start is inclusive stop is exclusive
first_name = name[:8] # same thing
print(first_name)
last_name = name[8:14]
last_name = name[8:]
print(last_name)
weird_name = name[0:14:2] # uses every second character in name, defaults to step of 1
weird_name = name[::2] # same thing start and stop are beginning and end
print(weird_name)
reversed_name = name[::-1]
print(reversed_name)

website1 = "https://www.google.com"
website2 = "https://www.youtube.com"

slice = slice(12,-4) # creating slice object named slice and invoking slice function
print(website1[slice])
print(website2[slice])