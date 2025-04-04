# Deque=> Deque implementing using singly linked list.

# Time complexity=>
# 1) append , Tn=O(1)
# 2) pop , Tn=O(1)
# 3) appendLeft , Tn=O(1)
# 4) popRight , Tn=O(n)
# 5) empty , Tn=O(1)
# 6) peek , Tn=O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:

    def __init__(self):
        self.head = self.tail = None

    def append(self, data):
        newData = Node(data)
        if self.empty():
            self.head = self.tail = newData
        else:
            self.tail.next = newData
            self.tail = newData

    def pop(self):
        if self.empty():
            return -1
        else:
            remData = self.head.data
            self.head = self.head.next

    def appendLeft(self, data):
        newData = Node(data)
        if self.empty():
            self.head = self.tail = newData
        else:
            newData.next = self.head
            self.head = newData

    def popRight(self):
        if self.empty():
            return -1
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp != None and temp.next.next != None:
                temp = temp.next
            remData = temp.next.data
            temp.next = None
            return remData

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            return -1
        else:
            return self.head.data

    def printDeque(self):
        if self.empty():
            return print("Deque is empty!")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, "<--- Deque data")
                temp = temp.next