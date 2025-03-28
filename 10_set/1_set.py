# set=>
# i) set in python used to store multiple value in a varibale like list,but it created using curly {} braces.
# ii) set is unchangeble we can not change the stored value of set but can add new item in it and can delete existing one.
# iii) set always store unique value in set.
# iv) set does not follow order to store value in it.
#  v) in set ,we cannot access the data using indexing unlike list , touple only we can access using the loop.

# Syntax=>
my_set = {2, 3, True, "Jitesh", False, 0}
print(my_set)


# i) length of set=>
length = len(my_set)
print(length)

# ii) accessing data using loop=>
for i in my_set:
    print(i)

# iii) adding new items to set=>
my_set.add(10)
my_set.add(11)

# iv) removing item from set=> remove("item name"), discard("item name") and pop() for removing data from set.

my_set.remove(10)
for i in my_set:
    print(i)

