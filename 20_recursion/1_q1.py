# Q1- Print the 1 to 10?


def printNaturalNum(n):
    def helper(i):
        if i > n:
            return
        else:
            helper(i + 1)
            print(i)

    i = 1
    helper(i)

printNaturalNum(10)
