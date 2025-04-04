class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None

    def empty(self):
        return self.head == None

    def append(self, data):
        newData = Node(data)
        newData.next = self.head
        self.head = newData

    def pop(self):
        if self.empty():
            return -1
        else:
            remData = self.head.data
            self.head = self.head.next
            return remData

    def peek(self):
        if self.empty():
            return -1
        else:
            return self.head.data

    def printStack(self):
        if self.empty():
            return print("Stack is empty!")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next