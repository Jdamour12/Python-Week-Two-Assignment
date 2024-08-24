# Creating empty list
my_list = []

# Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position of my_list
my_list.insert(1, 15)

# Extending my_list with other list called other_list
other_list = [50, 60, 70]
my_list.extend(other_list)

# Removing the last element from my_list
del my_list[-1]

# Sorting my_list in ascending order by using sort() function
my_list.sort()

# Printing my_list
print(f'All elements in my_list are: {my_list}', end="\n\n")

# finding and printing the index of the value 30 in my_list
print(f'Index of the value 30 in my_list is: {my_list.index(30)}')
