class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = self.tail = None

    def append(self, data):
        newData = Node(data)
        if self.head == None and self.tail == None:
            self.head = self.tail = newData
        else:
            self.tail.next = newData
            newData.prev=self.tail
            self.tail = newData

    def appendLeft(self, data):
        newData = Node(data)
        if self.head == None and self.tail == None:
            self.head = self.tail = newData
        else:
            newData.next = self.head
            self.head.prev = newData
            self.head=newData

    def popRight(self):
        if self.head == None:
            return -1
        elif self.head.next == None:
            self.head = self.tail = None
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return

    def popLeft(self):
        if self.head == None:
            return -1
        else:
            self.head = self.head.next
            self.head.prev = None

    def empty(self):
        return self.head == None

    def printDeque(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next