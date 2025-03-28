# Lists=> list is like array.
# Syntax=>
list = []

# Operations in lists=>

# i) append in lists=> adding data in list.
list.append(1)
list.append(2)
list.append(3)
list.append(2)
list.append(3)

# ii) pop from lists=> deleting data from list.
list.pop(2)
# or
list.pop()

# iii) length of lists=>
length = len(list)
print(length)

# iv) loop over lists=>
for i in list:
    print(i)


# Note=>
# i) lists follow references rules.
# ii) lists can have duplicates data.
# iii) lists always follow the order, mean if any data added or deleted then it will not affect the main lists of orders.
# iv) lists can also created using the constructor
# ex-1
myList = list((1, 2, 3, 4))
print(myList)
