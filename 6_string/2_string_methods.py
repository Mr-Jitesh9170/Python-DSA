# 1. Loop over array=>
# Example-1
data = "Jitesh pandey"
for i in data:
    print(i)

# 2. Getting string data using index=>
# Example-2
print(data[2])

# 3. String length=>
# Example-3
print(len(data))

# 4. Converting in upper()=>
print(data.upper())

# 5. Converting in lower()=>
print(data.lower())

# 6. Removing extra space from string=>
print(f" {data} ".strip())

# 7. Splitting string in form of array=>
print(data.split(","))

# 8. Concatenation string=>
a = "Jitesh"
b = "Pandey"
print(a + " " + b)


# 9. Formate string(string literal)=>
name = "Jitesh!"
greeting = f"Hey ,{name}"
print(greeting)