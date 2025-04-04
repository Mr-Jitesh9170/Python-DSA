class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    # add first=>
    def appendLeft(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size += 1

    # remove first=>
    def popLeft(self):
        if self.head is None:
            return print("DLL is empty!")
        elif self.head.next == None:
            removedData = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return removedData
        else:
            removedData = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return removedData

    # add last=>
    def appendRight(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1

    # remove last=>
    def popRight(self):
        if self.head == None and self.tail == None:
            return print("DLL is empty!")
        elif self.head.next == None:
            removedData = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return removedData
        else:
            removeData = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return removeData

    # print dll=>
    def printLinkedList(self):
        temp = self.head
        if temp is None:
            return print("DLL is empty!")
        while temp is not None:
            print(temp.data, end=" <--> ")
            temp = temp.next
        else:
            print(None)