# Touple=> tuple stores multiple data like lists.

# Syntax=> To create single value in tuple we have to use of commo after single data.
# Exampl-1
touple = (1,)
print(touple)
# Example-2
touple = (1, 2, 3, 4, 5)

# i) accessing touple items using index=>
print(touple[0])

# ii) loop over touple=>
for i in touple:
    print(i)

# iii) length of touple=>
length = len(touple)
print(length)

# iv) changing value of touple=>
mylist = list(touple)
mylist.append(5)
touple = tuple(mylist)
print(touple)


# Note=>
# i) touple in python it immutable , we can not change the data of it, if is once assigned.
# ii) only way to change the data fo touple to converting touple in list , performing list operation and back convert list to touple.
# iii) touple can have duplicate values as well.
