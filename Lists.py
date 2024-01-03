# List - store multiple items in a single variable

food = ["pizza", "hamburgers", "hotdog", "ramen"]
food[0] = "sushi"
print(food)
print(food[0])

food.append("ice cream") # add to the end
food.remove("hotdog")
food.pop() # removes the last element
food.insert(1, "cake")
food.sort() # sort list alphabetically

for x in food:
    print(x)

food.clear()