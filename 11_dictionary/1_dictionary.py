# Dictionary => dictionary in python is like object in javascript.

# Note =>
# i)dictionary contains data in form of the key and value pair.
# ii)dictionary does not contain duplicate data.
# iii)dictionary alway maintains their order.
# iv)Dictionary follow the rule of referencing.
# v)In dictionary we can performin add , update , and delete operations.

# Syntax =>
userDetails = {
    "firstName": "Jitesh",
    "lastName": "Pandey",
    "age": 23,
    "qualifications": "B.tech(computer science and engineering)",
}

# Operations =>

# 1. Accessing items
print(userDetails.get("firstName"))
# OR
print(userDetails["firstName"])

# 2. Adding new items
userDetails["color"] = "gora"
print(userDetails)
# OR
userDetails.update({"color": "gora"})
print(userDetails)

# 3. Updating existing data
userDetails["firstName"] = "Jay"
print(userDetails)
# OR
userDetails.update({"age": 20})
print(userDetails)


# 4. Deleting items
del userDetails["qualifications"]
print(userDetails)
# OR
userDetails.pop("age")
print(userDetails)

# 5. Loop over dictionary
for i in userDetails:
    print(userDetails[i])
