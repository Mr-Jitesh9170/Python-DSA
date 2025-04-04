class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            removedData = self.stack.pop()
            return removedData

    def empty(self):
        if len(self.stack):
            return False
        else:
            return True

    def peek(self):
        if self.empty():
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    def printStack(self):
        if self.empty():
            print("Stack is empty!")
        for i in self.stack:
            print(i) 