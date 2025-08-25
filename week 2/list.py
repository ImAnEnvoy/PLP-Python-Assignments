
# Question 1: Greating an empty list
my_list = []

# Question 2: Elements to be apended to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Question 3: Inserting 15 at the second position in the list
my_list.insert(2,15)
print(my_list)

# Question 4: Extend my_list with another list [50,60,70]
new_list = [50, 60, 70]  # Assigning new list

my_list.extend(new_list)  # Extending my_list
print(my_list)

# Question 5: Remove the last element from my_list
my_list.pop()
print(my_list)

# Question 6: Sorting my_list in ascending order

# Find and print the index of the value 30 in my_list
print(my_list.index(30))
