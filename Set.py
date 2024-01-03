# Set - collection that is unordered and unindexed, no duplicate values.
# sets are faster than lists and it is quicker to see if there is an item in a set compared to a list
# if there are duplicate items, they will be ignored when printing

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin") # add an element to set
utensils.remove("fork") # remove element from set
utensils.update(dishes) # add all elements in dishes to utensils set

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) # prints what utensils has that dishes does not
print(utensils.intersection(dishes)) # prints what utensils has in common with dishes

for x in utensils:
    print(x) # see how the order they are printed in changes

utensils.clear() # removes all elements from set