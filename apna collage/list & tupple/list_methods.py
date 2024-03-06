# Create an empty list
my_list = []

# append(), extend(), insert(), remove(), pop(), clear(), sort(), and reverse()
# above function will return null value so.
# i will change the original list.

# Append an item to the end of the list
my_list.append(5)
print("After appending:", my_list)

# Extend the list by appending elements from another iterable
my_list.extend([6, 7, 8])
print("After extending:", my_list)

# Insert an item at a specified position
my_list.insert(1, 10)
print("After inserting:", my_list)

# Remove the first occurrence of an item from the list
my_list.remove(6)
print("After removing:", my_list)

# Remove and return the item at the specified position
popped_item = my_list.pop(2)
print("Popped item:", popped_item)
print("After popping:", my_list)

# Clear all items from the list
my_list.clear()
print("After clearing:", my_list)

# Index of the first occurrence of an item in the list
if my_list:
    index = my_list.index(5)
    print("Index of 5:", index)
else:
    print("List is empty.")

# Count the number of occurrences of an item in the list
if my_list:
    count = my_list.count(5)
    print("Count of 5:", count)
else:
    print("List is empty.")


# Sort the items of the list in place
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print("After sorting:", my_list)

# Reverse the elements of the list in place
my_list.reverse()
print("After reversing:", my_list)

# Shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)
