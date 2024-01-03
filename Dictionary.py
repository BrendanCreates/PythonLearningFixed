# Dictionary - A changable unordered collection of unique key:value pairs
# they are fast because they use hashing, they allow access to a value quickley

capitals = {'USA':'Washington',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['Russia'])
# print(capitals['Germany'])  Will throw errors
print(capitals.get('Germany')) # Will return None instead
print(capitals.keys()) # prints all of the keys
print(capitals.values()) # prints all of the values
print(capitals.items()) # prints the entire dictionary
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
for key,value in capitals.items():
    print(key, value) # prints all the items in the dictionary
capitals.clear()