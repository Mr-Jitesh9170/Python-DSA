pattern = "hello world"
alphabet = "abcdefghijklmnopqrstuvwxyz"
data = ""

for i in range(len(pattern)):
    for j in alphabet:
        if pattern[i] == j:
            data += j
            print(data)
        elif pattern[i] == " ":
            data += " "
            break
        else:
            print(data)
